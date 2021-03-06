from django.contrib.auth.models import User
from django import forms
from .models import BlogPost


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'tags']


class BlogPostForm(forms.Form):
    author = forms.CharField(label="Author")
    title = forms.CharField(label="Title", max_length=255)
    content = forms.CharField(widget=forms.Textarea)
    tags = forms.CharField(label="Tags")


class CommentsForm(forms.Form):
    email = forms.EmailField(label="Email")
    content = forms.CharField(widget=forms.Textarea, label="Content")
