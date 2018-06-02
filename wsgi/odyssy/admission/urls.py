from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<programme>[-\w]+)/$', views.view_admission_programme, name='admission'),
    url(r'^$', views.view_admission, name='admission-html')
]
