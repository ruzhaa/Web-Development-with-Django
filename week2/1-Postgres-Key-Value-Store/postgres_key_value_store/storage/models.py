import uuid
from django.db import models


class User(models.Model):
    identifier = models.UUIDField(primary_key=True, default=uuid.uuid4)


class KeyValue(models.Model):
    key = models.CharField(max_length=255)
    value = models.TextField()
    user = models.ForeignKey(User, related_name='data')
