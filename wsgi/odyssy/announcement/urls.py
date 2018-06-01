from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<announcement_slug>[-\w]+)/$', views.open_view, name='announcement-view-single'),
    url(r'^$', views.index, name='all_announcements'),
]
