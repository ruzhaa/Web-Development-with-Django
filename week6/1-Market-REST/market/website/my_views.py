from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm, AddOfferForm, AddOfferModelForm
from .models import Category, Offer


def index(request):
    offers = Offer.objects.select_related('category', 'author').all()
    return render(request, 'website/index.html', locals())


@login_required(login_url=reverse_lazy('login'))
def add_offer(request):
    form = AddOfferForm()

    if request.method == 'POST':
        form = AddOfferForm(data=request.POST)
        if form.is_valid():
            new_offer = Offer.objects.create(**form.cleaned_data)
            return redirect(reverse('index'))
    return render(request, 'website/add_offer.html', locals())


def registration_view(request):
    form = RegistrationForm()

    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)

            return redirect(reverse('index'))
        else:
            alert = form.errors
            return render(request, 'website/registration.html', {'alert': alert})
    return render(request, 'website/registration.html', locals())


# def login_view(request):
#     form = LoginForm()

#     if request.user.is_authenticated:
#         return redirect(reverse('index'))

#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)

#             if user is not None:
#                 login(request, user)
#                 return redirect(reverse('index'))
#         else:
#             alert = form.errors
#             return render(request, 'registration/login.html', {'alert': alert})
#     return render(request, 'registration/login.html', locals())


# @login_required
# def logout_view(request):
#     logout(request)
#     return redirect(reverse('index'))
