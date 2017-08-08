from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'student_corner.html$', views.IndexView.as_view(), name="student_corner"),
	url(r'^student_corner/(?P<pk>\d+)/$', views.DetailView.as_view(), name="detail"),
    url(r'.html$', views.view_more, name='more-html')

]
