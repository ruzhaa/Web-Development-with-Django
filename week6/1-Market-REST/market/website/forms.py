from django.contrib.auth.models import User
from django import forms
from .models import Offer


class AddOfferModelForm(forms.Form):
    class Meta:
        models = Offer
        fields = ['title', 'price', 'category', 'descrioption', 'author', 'created_date', 'image']


class AddOfferForm(forms.Form):
    title = forms.CharField(label='title')
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    description = forms.CharField(widget=forms.Textarea)
    # image = forms.FileUpload()
    category = forms.ChoiceField()


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(widget=forms.PasswordInput())
