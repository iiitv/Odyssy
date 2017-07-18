from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<announcement_id>[0-9]+)/$', views.open_view, name='open-view'),
    url(r'^$', views.index, name='all_announcements'),
]
