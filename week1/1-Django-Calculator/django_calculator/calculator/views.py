from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.


def sumNumbers(request, a, b):
    a = int(a)
    b = int(b)
    my_format = request.GET.get('format', '')
    if my_format.lower() == 'json':
        data = {
            'result': a + b
        }
        return JsonResponse(data)
    return HttpResponse(a + b)


def multiply(request, a, b):
    a = int(a)
    b = int(b)
    my_format = request.GET.get('format', '')
    if my_format.lower() == 'json':
        data = {
            'result': a * b
        }
        return JsonResponse(data)
    return HttpResponse(a * b)


def power(request, a, b):
    a = int(a)
    b = int(b)
    my_format = request.GET.get('format', '')
    if my_format.lower() == 'json':
        data = {
            'result': a ** b
        }
        return JsonResponse(data)
    return HttpResponse(a**b)


def fact(request, a):
    factoriel = 1
    num = int(a)
    while num != 1 and num != 0:
        factoriel *= num
        num -= 1
    my_format = request.GET.get('format', '')
    if my_format.lower() == 'json':
        data = {
            'result': factoriel
        }
        return JsonResponse(data)
    return HttpResponse(factoriel)
