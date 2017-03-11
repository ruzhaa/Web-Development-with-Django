from django.conf.urls import url
from . import views
import re

UUID4_REGEX = re.compile('([a-zA-Z]|[0-9]){8}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){12}')

urlpatterns = [
    url(r'^storage/create-user', views.create_user),
    url(r'^storage/(?P<user_identifire>([a-zA-Z]|[0-9]){8}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){12})', views.storage_user_identifire),

]
