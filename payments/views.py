import re
from PIL import Image
import pytesseract
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Transaction

def payment(request):
    if request.method == 'POST' and request.FILES['payment_screenshot']:
        # Save the uploaded screenshot to server storage
        payment_screenshot = request.FILES['payment_screenshot']
        fs = FileSystemStorage()
        screenshot_path = fs.save(f'payments/{payment_screenshot.name}', payment_screenshot)
        screenshot_url = fs.url(screenshot_path)

        # Extract transaction ID from the uploaded screenshot (using OCR)
        transaction_id = extract_transaction_id_from_screenshot(screenshot_path)
        
        # Check if the transaction ID is valid and if it already exists in the database
        if transaction_id and not transaction_exists(transaction_id):
            # Mark the user as a member
            user = request.user
            user.profile.is_member = True  # Assuming there's a field `is_member` in the user's profile
            user.profile.save()

            # Mark the transaction as processed
            save_transaction(transaction_id)

            return redirect('membership_success')  # Redirect to a success page
        else:
            return redirect('payment_failed')  # Redirect to a failure page (optional)

    return render(request, 'payment.html')


def extract_transaction_id_from_screenshot(screenshot_path):
    # Use OCR to extract text from the image (transaction ID)
    img = Image.open(screenshot_path)
    text = pytesseract.image_to_string(img)

    # Check if '100' is present in the extracted text
    if '90' not in text:
        return None  # Fail if '100' is not in the text

    # Assuming the transaction ID is a 7-character string with a mix of letters and numbers
    match = re.search(r'[A-Za-z0-9]{7}', text)  # Regex for 7-character alphanumeric transaction ID
    if match:
        return match.group(0)
    return None


def transaction_exists(transaction_id):
    # Check if the transaction ID already exists in the database
    return Transaction.objects.filter(transaction_id=transaction_id).exists()


def save_transaction(transaction_id):
    # Save the transaction to the database to prevent it from being reused
    transaction = Transaction(transaction_id=transaction_id)
    transaction.save()


def membership_success(request):
    return render(request, 'membership_success.html')

def payment_failed(request):
    return render(request, 'payment_failed.html')
