# forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['photo', 'caption']
        widgets = {
            'caption': forms.Textarea(attrs={'placeholder': 'Write a caption...', 'rows': 3, 'cols': 20}),
        }

