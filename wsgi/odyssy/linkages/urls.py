from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.linkage, name='linkage-all'),
    url(r'^(?P<link_id>[0-9]+)/$', views.linkage_detail, name='linkage-single')
]
