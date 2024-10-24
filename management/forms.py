from django import forms
from django.contrib.auth.models import User
from .models import Comment,Post
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ['text']
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['view']