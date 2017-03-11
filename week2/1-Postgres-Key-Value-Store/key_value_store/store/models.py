import uuid
from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class KeyValue(models.Model):
    key = models.CharField(max_length=300)
    value = models.CharField(max_length=300)
    user_id = models.ForeignKey(User)
