from django.conf.urls import url
from django.contrib.auth.views import login, logout
from .my_views import registration_view

from .views import (
    OfferListView,
    CreateOfferView,
    UpdateOfferView,
    OfferView,
    DeleteOfferView,
    PendingListView,
    OfferAcceptView,
    ApprovedAndRejectedListView
)

urlpatterns = [
    url(r'^$', OfferListView.as_view(), name='index'),
    url(r'^pending-offers', PendingListView.as_view(), name='pending-offers'),
    url(r'^approved-rejected', ApprovedAndRejectedListView.as_view(), name='approved-rejected'),
    url(r'^add-offer', CreateOfferView.as_view(), name='add-offer'),
    url(r'^offer/edit/(?P<pk>[0-9]+)', UpdateOfferView.as_view(), name='edit-offer'),
    url(r'^offer/(?P<pk>[0-9]+)', OfferView.as_view(), name='offer-view'),
    url(r'^delete/(?P<pk>[0-9]+)$', DeleteOfferView.as_view(), name='delete-offer'),

    url(r'^accept/(?P<pk>[0-9]+)', OfferAcceptView.as_view(), name='accept-offer'),

    # url(r'^statistics/$', get_statistics, name='statistics'),
    url(r'^registration/$', registration_view, name='registration-view'),
    url(r'^login/$', login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout')
]
