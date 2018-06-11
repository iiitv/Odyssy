from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.all_programme, name='all-programme'),
    url(r'^(?P<name>[-\w.]+)/(?P<branch>[-\w]+)/$', views.single_programme, name='single-programme'),
    url(r'^(?P<name>[-\w.]+)/(?P<branch>[-\w]+)/(?P<semester>[-\w]+)/(?P<course_code>[-\w]+)/$', views.single_course,
        name='single-course'),
    url(r'^(?P<name>[-\w.]+)/$', views.view_phd, name='view-phd')
]
