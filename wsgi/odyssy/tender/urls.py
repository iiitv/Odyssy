from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.view_tender, name='active-tender'),
    url(r'^archive/$', views.view_archive, name='archive-tender')
]
