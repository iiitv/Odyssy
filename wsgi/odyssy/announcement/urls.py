from django.conf.urls import url

from . import views

urlpatterns = [ # pylint: disable=invalid-name
    url(r'^(?P<announcement_id>[0-9]+)/$', views.open_view, name='open-view'),
    url(r'^$', views.index, name='index-view'),
]
