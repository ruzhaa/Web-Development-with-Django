from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Offer(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    category = models.ForeignKey(Category, related_name="category")
    description = models.TextField()
    author = models.ForeignKey(User, related_name="author")
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField()
