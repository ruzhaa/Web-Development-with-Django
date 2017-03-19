from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .exceptions import UserDoesNotExist
from .services import (
    count_users,
    count_keys,
    get_all_users,
    get_user,
    get_key_value_for_user,
    set_key,
)


def index(request):
    total_number = count_users()
    total_keys = count_keys()

    users = get_all_users()
    return render(request, 'index.html', locals())


def user_detail(request, identifier):
    user = get_user(identifier)
    set_of_key_value = get_key_value_for_user(identifier)
    for kv in set_of_key_value:
        key = kv.key
        value = kv.value
        created_at = kv.created_at

    return render(request, 'user_detail.html', locals())


def add_key(request, identifier):
    if request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')

        try:
            set_key(identifier=identifier, key=key, value=value)
        except UserDoesNotExist:
            error = {
                'error': 'User not found'
            }
            return HttpResponse(error, status=404)
        url = reverse('user-detail', kwargs={'identifier': identifier})
        return redirect(url)
    return render(request, 'add_key.html')
