from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^faculty/$', views.faculty, name='faculty'),
    url(r'^visiting_faculty/$', views.visiting_faculty, name='visiting_faculty'),
    url(r'^staff/$', views.staff, name='staff'),
    url(r'^(?P<slug>[-\w]+)/$', views.details, name='details')
]
