from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.open_all_news, name='news-all'),
    url(r'^(?P<news_id>[0-9]+)/$', views.open_single_news, name='news-single')
]
