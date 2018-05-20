from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^add/(?P<data_type>.+)$', views.add, name='add_data'),
]
