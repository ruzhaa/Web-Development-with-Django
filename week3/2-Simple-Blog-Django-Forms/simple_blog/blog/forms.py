from django import forms
from .models import BlogPost


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'tags']


class BlogPostForm(forms.Form):
    title = forms.CharField(label="Title", max_length=255)
    content = forms.CharField(widget=forms.Textarea)
