from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.all_committee, name='all-committee'),
    url(r'^(?P<committee_name>[-\w]+)/', views.single_committee, name='committee-single'),
    url(r'.html/$', views.view_institute, name='committee-html')
]
