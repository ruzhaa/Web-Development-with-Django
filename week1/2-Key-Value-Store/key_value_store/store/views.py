from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import uuid
import json

# Create your views here.


def create_uuid():
    return str(uuid.uuid4())


def read_json():
    with open('users.json', 'r') as f:
        data = json.load(f)
    return data


def create_user(request):
    if request.method == 'GET':

        my_identifier = create_uuid()

        data = read_json()
        dic = {my_identifier: {}}
        data.update(dic)

        with open('users.json', 'w') as f:
            json.dump(data, f)
        return JsonResponse({"identifier": my_identifier})

    return HttpResponse(status=405)


def storage_user_identifire(request, *args, **kwargs):
    if request.method == 'POST':
        print(request)
        body = request.body.decode('utf-8')
        body = json.loads(body)
        n = body['key']
    return HttpResponse(status=405)
