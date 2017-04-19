from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import Offer
from .serializers import OfferSerializer


class APIOfferListView(ListAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class APIPendingListView(ListAPIView):
    queryset = Offer.objects.get_pending_offers()
    serializer_class = OfferSerializer


class APIApprovedAndRejectedListView(ListAPIView):
    queryset = Offer.objects.get_approved_and_rejected_offers()
    serializer_class = OfferSerializer


class APIOfferSetView(RetrieveUpdateDestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class APICreateOfferView(CreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
