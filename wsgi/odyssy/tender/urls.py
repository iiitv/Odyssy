from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'.html$', views.view_tender, name='tender')
]
