from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<programme>[a-zA-Z]+)/$', views.view_admission_programme, name='admission'),
    url(r'.html$', views.view_admission, name='admission-html')
]
