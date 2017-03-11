import json

from django.http import JsonResponse, HttpResponse
from .models import User, KeyValue


def create_user_view(request):
    identifier = User.objects.create()
    # key_value = KeyValue.objects.create(key='', value='', user_id=identifier)

    return JsonResponse({'identifier': identifier.id})


def set_key_view(request, identifier):
    try:
        user_identifier = User.objects.get(id=identifier)
        get_key_value = KeyValue.objects.get(user_id=user_identifier)
        body = request.body.decode('utf-8')
        payload = json.loads(body)
        if get_key_value.key is '':
            new_key_value = KeyValue.objects.create(
                key=payload['key'],
                value=payload['value'],
                user_id=user_identifier)
            new_key_value.save()
        else:
            get_key_value.key = payload['key']
            get_key_value.value = payload['value']
            get_key_value.save()
    except User.DoesNotExist:
        error = {
            'error': 'User not found'
        }
        return JsonResponse(error, status=404)
    except KeyValue.DoesNotExist:
        error = {
            'error': 'KeyValue not found'
        }
        return JsonResponse(error, status=404)
    return JsonResponse(payload, status=201)


def manage_key_view(request, identifier, key):
    if request.method == 'GET':
        return get_key_view(request, identifier, key)

    if request.method == 'DELETE':
        return delete_key_view(request, identifier, key)

    return HttpResponse(status=405)


def get_key_view(request, identifier, key):
    try:
        user = User.objects.get(id=identifier)
        get_value = KeyValue.objects.get(user_id=user, key=key)
    except User.DoesNotExist:
        error = {
            'error': 'User not found'
        }
    except KeyValue.DoesNotExist:
        error = {
            'error': 'key not found'
        }
        return JsonResponse(error, status=404)

    if get_value.value is None:
        error = {
            'error': 'key not found'
        }
        return JsonResponse(error, status=404)

    return JsonResponse({'value': get_value.value}, status=200)


def delete_key_view(request, identifier, key):
    try:
        user = User.objects.get(id=identifier)
        get_value = KeyValue.objects.get(user_id=user, key=key)

        value = get_value.value
        get_value.delete()
        get_value.save()
    except User.DoesNotExist:
        error = {
            'error': 'User not found'
        }
    except KeyValue.DoesNotExist:
        error = {
            'error': 'key not found'
        }
        return JsonResponse(error, status=404)

    if value is None:
        error = {
            'error': 'key not found'
        }
        return JsonResponse(error, status=404)
    return JsonResponse({'value': value}, status=202)
