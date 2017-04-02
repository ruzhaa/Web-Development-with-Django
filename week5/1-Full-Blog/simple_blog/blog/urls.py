from django.conf.urls import url
from .views import (
    index,
    show_post,
    create_new_post,
    registration_view,
    login_view,
    logout_view
)


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^show-post/(?P<title>.*)', show_post, name='show-post'),
    url(r'^create-new-post/$', create_new_post, name='create-new-post'),
    url(r'^registration/$', registration_view, name='registration-view'),
    url(r'^login/$', login_view, name='login-view'),
    url(r'^logout/$', logout_view, name='logout-view')
]
