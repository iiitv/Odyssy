from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^add/(?P<data_type>.+)$', views.add, name='add_data'),
    url(r'^new/user/$', views.signup, name='create_new_user'),
    url(r'^view/users/(?P<msg>.+)$', views.all_users, name='all_users'),
    url(r'^list/(?P<data_type>.+)/(?P<msg>.+)$', views.ane_list, name='ane_list'),
    url(r'^edit/(?P<data_type>.+)/(?P<data_id>.+)$', views.ane_edit, name='ane_edit'),
    url(r'^user/(?P<username>.+)/edit$', views.edit_user, name='edit_user'),
    url(r'^delete/(?P<data_type>.+)/(?P<data_id>.+)$', views.ane_delete, name='ane_delete'),
    url(r'^change/password$', views.change_password, name='change_password'),
]
