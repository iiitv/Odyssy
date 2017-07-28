from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name="gallery"),
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name="detail")
]
