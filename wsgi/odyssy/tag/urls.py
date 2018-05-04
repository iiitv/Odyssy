from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^(?P<tag_name>([a-zA-Z0-9][a-zA-Z0-9\-]{3,})+)/$',
        views.simple_tag, name='simple-tag'),
    url(r'^(?P<tag_name>([a-zA-Z0-9][a-zA-Z0-9\-]{3,})+)/announcement/$',
        views.announcement_tag, name='announcement-tag'),
    url(r'^(?P<tag_name>([a-zA-Z0-9][a-zA-Z0-9\-]{3,})+)/news/$',
        views.news_tag, name='news-tag'),
    url(r'^(?P<tag_name>([a-zA-Z0-9][a-zA-Z0-9\-]{3,})+)/pictures/$',
        views.picture_tag, name='picture-tag'),
]
