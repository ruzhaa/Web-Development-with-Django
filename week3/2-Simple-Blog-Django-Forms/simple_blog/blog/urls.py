from django.conf.urls import url
from .views import index, show_post, create_new_post


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^show-post/(?P<title>.*)', show_post, name='show-post'),
    url(r'^create-new-post/$', create_new_post, name='create-new-post'),
]
