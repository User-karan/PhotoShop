from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from gallery.forms import PostForm
from gallery.models import Post  # Fix: Corrected the typo here


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Handle files
        if form.is_valid():
            post = form.save(commit=False)
            post.account = request.user  # Link the post to the logged-in user
            post.save()  # Save the post to the database
            return redirect('gallery')  # Redirect to gallery after post creation
        else:
            # Log errors if the form is not valid
            print(form.errors)  # You can log this in a log file if needed
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})
