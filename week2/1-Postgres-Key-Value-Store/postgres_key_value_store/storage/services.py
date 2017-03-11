import os
import uuid
import json

from django.conf import settings
from .exceptions import UserDoesNotExist
from .models import User, KeyValue


def write_user_database(identifier, data):
    identifier_json = identifier + '.json'
    path = os.path.join(settings.JSON_DATABASE_DIR, identifier_json)

    with open(path, 'w') as f:
        f.write(json.dumps(data, indent=4))


def create_uuid():
    user = User.objects.create()
    return str(user.identifier)


def create_user():
    identifier = create_uuid()
    write_user_database(identifier, data={})

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
