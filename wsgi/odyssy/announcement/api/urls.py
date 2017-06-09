from django.conf.urls import url

from .views import (
    AnnouncementListView,
    AnnouncementParticularView,
    AnnouncementTagView,
    AnnouncementLatestView,
)

urlpatterns = [
    url(r'^$', AnnouncementListView.as_view(),  name='all-announcement'),
    url(r'^(?P<key>\d+)/$', AnnouncementParticularView.as_view(), name='particular-announcement'),
    url(r'^tag/(?P<tag_name>[\w\s]+)/$', AnnouncementTagView.as_view(), name='tag-announcement'),
    url(r'^latest/(?P<cnt>\d+)/$', AnnouncementLatestView.as_view(), name='latest-announcement'),
]
