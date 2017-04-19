from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Offer


class BaseUserPassesTestMixin(UserPassesTestMixin):

    def test_func(self):
        return True


class CanUpdateOfferMixin(BaseUserPassesTestMixin):

    def test_func(self):
        offer_id = self.kwargs.get('pk')
        offer = Offer.objects.get(id=(offer_id))

        if not offer.author == self.request.user:
            return False
        return True and super().test_func()


class IsSuperUserMixin(BaseUserPassesTestMixin):

    raise_exception = True

    def test_func(self):
        if not self.request.user.is_superuser:
            return False

        return True and super().test_func()
