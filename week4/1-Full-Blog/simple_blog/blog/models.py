from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Tags(models.Model):
    tag = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.tag


class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    authors = models.ManyToManyField(User, related_name='author')
    tags = models.ManyToManyField(Tags, related_name='posts')

    def __str__(self):
        return self.title


class Comment(models.Model):
    author_email = models.EmailField()
    created_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    blog_post = models.ForeignKey(BlogPost, related_name="data")
