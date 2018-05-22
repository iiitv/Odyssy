from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^add/(?P<data_type>.+)$', views.add, name='add_data'),
    url(r'^list/(?P<data_type>.+)/(?P<msg>.+)$', views.ane_list, name='ane_list'),
    url(r'^edit/(?P<data_type>.+)/(?P<data_id>.+)$', views.ane_edit, name='ane_edit'),
    url(r'^delete/(?P<data_type>.+)/(?P<data_id>.+)$', views.ane_delete, name='ane_delete'),
]
