from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.news, name='news-all'),
    url(r'^(?P<news_slug>[-\w]+)/$', views.news_detail, name='news-single')
]
