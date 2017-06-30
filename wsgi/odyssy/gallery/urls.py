from django.conf.urls import url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy

from . import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name="gallery"),
]
 
