from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from .forms import RegistrationForm
from .models import Offer
from .mixins import IsSuperUserMixin


class OfferView(DetailView):
    model = Offer
    template_name = 'website/offer_view.html'


class OfferListView(ListView):
    model = Offer
    queryset = Offer.objects.get_approved_offers()
    template_name = 'website/offer_list.html'


class PendingListView(LoginRequiredMixin, IsSuperUserMixin, ListView):
    model = Offer
    queryset = Offer.objects.get_pending_offers()
    template_name = 'website/offer_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['pending'] = True
        return context


class OfferAcceptView(LoginRequiredMixin, IsSuperUserMixin, UpdateView):
    model= Offer
    template_name = 'website/offer_list.html'


class ApprovedAndRejectedListView(ListView):
    model = Offer
    queryset = Offer.objects.get_approved_and_rejected_offers()
    template_name = 'website/offer_list.html'


class CreateOfferView(LoginRequiredMixin, CreateView):
    model = Offer
    fields = ['title', 'description', 'category']
    template_name = 'website/offer_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('website:index')


class UpdateOfferView(LoginRequiredMixin, UpdateView):
    model = Offer
    fields = ("title", "description", "category")
    template_name = 'website/offer_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('website:index')


class DeleteOfferView(LoginRequiredMixin, DeleteView):
    model = Offer

    def get_success_url(self):
        return reverse_lazy('website:index')


def registration_view(request):
    form = RegistrationForm()

    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)

            return redirect(reverse('website:index'))
        else:
            alert = form.errors
            return render(request, 'website/registration.html', {'alert': alert})
    return render(request, 'website/registration.html', locals())
