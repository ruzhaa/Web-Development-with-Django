from django.conf.urls import url
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^calculator/add/([0-9]+)/([0-9]+)/$', views.sumNumbers),
    url(r'^calculator/multiply/([0-9]+)/([0-9]+)/$', views.multiply),
    url(r'^calculator/power/([0-9]+)/([0-9]+)/$', views.power),
    url(r'^calculator/fact/([0-9]+)/$', views.fact),
]
