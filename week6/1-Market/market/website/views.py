from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegistrationForm
from .models import Offer

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


class OfferListView(ListView):
    model = Offer


class CreateOfferView(LoginRequiredMixin, CreateView):
    model = Offer
    fields = ['title', 'description', 'category', 'image']
    template_name = 'website/offer_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('index')


class UpdateOfferView(LoginRequiredMixin, UpdateView):
    model = Offer
    fields = ("title", "description", "category")
    template_name = 'website/offer_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('index')


class OfferView(DetailView):
    model = Offer
    template_name = 'website/offer_view.html'


class OfferDeleteView(DeleteView):
    model = Offer

    def get_success_url(self):
        return reverse_lazy('index')


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
