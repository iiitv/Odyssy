from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^phd/$', views.phd, name='phd'),
    url(r'^faculty/$', views.faculty, name='faculty'),
    url(r'^former_faculty/$', views.former_faculty, name='former_faculty'),
    url(r'^visiting_faculty/$', views.visiting_faculty, name='visiting_faculty'),
    url(r'^staff/$', views.staff, name='staff'),
    url(r'^tag/(?P<tag>[-\w]+)/$', views.filter_by_tag, name='filter_by_tag'),
    url(r'^(?P<slug>[-\w]+)/$', views.details, name='details')
]
