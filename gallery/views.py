from django.shortcuts import render,redirect
from accounts.models import Account
from .models import Post,Comments
# Create your views here.
from django.shortcuts import get_object_or_404
from .forms import CommentForm,PostForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def gallery(request):
    # You can pass all posts to the gallery page if needed
    posts = Post.objects.all()
    return render(request, 'gallery.html', {'posts': posts})

@login_required
def post_detail(request, slug, username):
    post = get_object_or_404(Post, account__username=username, slug=slug)
    comments = Comments.objects.all().filter(post=post)

    # Handle the POST request (form submission or AJAX)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()

            # Check if the request is an AJAX request
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                data = {
                    'username': comment.user.username,
                    'content': comment.content,
                    'created_at': comment.created_at.strftime("%b %d, %Y - %H:%M"),
                    'success': True
                }
                return JsonResponse(data)

            # If not an AJAX request, redirect to the same page
            return redirect('view_post', slug=slug, username=username)

    else:
        form = CommentForm()
    if request.method == "POST" and 'like' in request.POST:
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            post.like_count -= 1
        else:
            post.likes.add(request.user)
            post.like_count += 1
        
        post.save()

        # Return the updated like count as a JSON response (for AJAX)
        return redirect('view_post',slug=slug,username=username) 


    context = {'post': post, 'comments': comments, 'form': form}
    return render(request, 'post_detail.html', context)


