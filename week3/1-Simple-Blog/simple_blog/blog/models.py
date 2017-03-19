from django.db import models
from django.utils import timezone


class Tags(models.Model):
    tag = models.CharField(max_length=255, unique=True)


class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    tags = models.ManyToManyField(Tags, related_name='posts')


class Comment(models.Model):
    author_email = models.EmailField()
    created_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    blog_post = models.ForeignKey(BlogPost)
