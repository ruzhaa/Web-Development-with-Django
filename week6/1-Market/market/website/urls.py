from django.conf.urls import url
from django.contrib.auth.views import login, logout
from .my_views import (
    index,
    add_offer,
    registration_view,
)

from .views import OfferListView, CreateOfferView, UpdateOfferView, OfferView, OfferDeleteView

urlpatterns = [
    url(r'^$', OfferListView.as_view(), name='index'),
    url(r'^add-offer', CreateOfferView.as_view(), name='add-offer'),
    url(r'^offer/edit/(?P<pk>[0-9]+)', UpdateOfferView.as_view(), name='edit-offer'),
    url(r'^offer/(?P<pk>[0-9]+)', OfferView.as_view(), name='offer-view'),
    url(r'^delete/(?P<pk>[0-9]+)$', OfferDeleteView.as_view(), name='delete-offer'),
    # url(r'^statistics/$', get_statistics, name='statistics'),
    url(r'^registration/$', registration_view, name='registration-view'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout')
]
