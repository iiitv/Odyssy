from django.conf.urls import url

from office_orders import views


urlpatterns = [
    url(r'^$', views.view_office_orders, name='active-orders'),
    url(r'^archive/$', views.view_archive, name='archive-orders')
]
