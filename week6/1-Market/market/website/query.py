from django.db import models


class OffersQuerySet(models.QuerySet):

    def get_pending_offers(self):
        return self.filter(status='1')

    def get_approved_and_rejected_offers(self):
        return self.filter(status__in=['2', '3'])

    def get_approved_offers(self):
        return self.filter(status='2')
