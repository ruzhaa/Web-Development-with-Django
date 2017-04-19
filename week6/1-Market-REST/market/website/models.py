from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from .query import OffersQuerySet


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Offer(models.Model):
    OFFER_STATUS = (
        ('1', 'pending'),
        ('2', 'approved'),
        ('3', 'reject')
    )
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    category = models.ForeignKey(Category, related_name="category", null=True)
    description = models.TextField()
    author = models.ForeignKey(User, related_name="author", null=True)
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='media/', null=True)
    status = models.CharField(max_length=1, choices=OFFER_STATUS, default='1')

    objects = OffersQuerySet.as_manager()
