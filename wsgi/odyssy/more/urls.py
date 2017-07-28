from django.conf.urls import url

from . import views

<<<<<<< HEAD

urlpatterns = [
    url(r'.html$', views.view_more, name='more-html')
]
=======
urlpatterns = [
url(r'student_corner.html$', views.IndexView.as_view(), name="student_corner"),
	url(r'^student_corner/(?P<pk>\d+)/$', views.DetailView.as_view(), name="detail"),
    url(r'.html$', views.view_more, name='more-html')

]
>>>>>>> eb917ae2a3adc9475a977b3c0203f822e3300117
