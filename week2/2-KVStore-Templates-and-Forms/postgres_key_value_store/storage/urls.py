from django.conf.urls import url

from .views import index, user_detail, add_key

uuid_regex = '([a-zA-Z]|[0-9]){8}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){12}'

urlpatterns = [
    url(r'^$', index, name="userdetail"),
    url(r'^user-detail/(?P<identifier>{})/$'.format(uuid_regex), user_detail, name="userdetail"),
    url(r'^add-key/(?P<identifier>{})/$'.format(uuid_regex), add_key),
]
