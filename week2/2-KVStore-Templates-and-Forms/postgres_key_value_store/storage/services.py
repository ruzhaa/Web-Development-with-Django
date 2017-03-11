import os
import uuid
import json

from django.conf import settings
from .exceptions import UserDoesNotExist
from .models import User, KeyValue


def create_uuid():
    user = User.objects.create()
    return str(user.identifier)


def create_user():
    identifier = create_uuid()

    return identifier


def get_user(identifier):
    try:
        user = User.objects.get(identifier=identifier)
    except User.DoesNotExist:
        raise UserDoesNotExist

    return user


def set_key(*, identifier, key, value):
    user = get_user(identifier)

    try:
        key_value = KeyValue.objects.get(key=key, user=user)
        key_value.value = value
        key_value.save()
    except KeyValue.DoesNotExist:
        key_value = KeyValue.objects.create(key=key, value=value, user=user)

    return key_value


def get_key(*, identifier, key):
    user = get_user(identifier)

    return KeyValue.objects.filter(key=key, user=user).first()


def delete_key(*, identifier, key):
    key_value = get_key(identifier=identifier, key=key)

    if key_value is None:
        return None

    key_value.delete()

    return key_value.value


def count_users():
    return User.objects.count()


def count_keys():
    return KeyValue.objects.count()


def get_all_users():
    return User.objects.all()


def get_key_value_for_user(identifier):
    user = get_user(identifier)
    return KeyValue.objects.filter(user=user)
