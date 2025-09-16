from django.shortcuts import render
from .models import RefreshTime
from datetime import datetime, timedelta
import pytz
from gallery.models import Post

def home(request):
    # Define Nepal timezone
    nepal_timezone = pytz.timezone('Asia/Kathmandu')

    # Get current time in Nepal timezone (this is timezone-aware)
    now = datetime.now(nepal_timezone)

    # Calculate the end_time for the countdown (example: midnight of the next day)
    end_time = datetime(now.year, now.month, now.day, 23, 59, 59) + timedelta(days=1)

    # If end_time is naive (no timezone), make it timezone-aware
    if end_time.tzinfo is None:
        end_time = nepal_timezone.localize(end_time)

    # Ensure the RefreshTime object exists
    refresh_time, created = RefreshTime.objects.get_or_create(id=1)  # assuming there's only one object

    if created:
        refresh_time.last_refreshed = now
        refresh_time.save()

    if now - refresh_time.last_refreshed > timedelta(hours=24):
        refresh_time.last_refreshed = now
        refresh_time.save()

    # Define start_time (midnight of today)
    start_time = datetime(now.year, now.month, now.day, 0, 0, 0, 0)

    # Ensure start_time is timezone-aware if it's naive
    if start_time.tzinfo is None:
        start_time = nepal_timezone.localize(start_time)

    # Now all are timezone-aware and can be compared
    if now > end_time:
        # Handle your condition here if needed
        pass

    # Prepare context to send to the template
    context = {
        'start_time': start_time.strftime('%Y-%m-%dT%H:%M:%S'),
        'end_time': end_time.strftime('%Y-%m-%dT%H:%M:%S'),
        'top_posts': Post.objects.all().order_by('-like_count')[:3]
    }

    return render(request, 'home.html', context)


def competition(request):
    return render(request, "competition.html")

def membership(request):
    return render(request, "membership.html")
