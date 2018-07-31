from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        medel = Post
        fields = ['title','text']