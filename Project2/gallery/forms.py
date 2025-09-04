from django import forms
from .models import Comments,Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content']



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['photo', 'title']  # Add all necessary fields here

