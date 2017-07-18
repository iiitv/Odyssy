from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'btech_admission.html$', views.view_btech_admission, name='btech-admission'),
    url(r'.html$', views.view_admission, name='admission-html')
]
