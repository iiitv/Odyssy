from django.conf.urls import url

import views

urlpatterns = [
    url(r'.html/$', views.serve_static, name='serve-static'),
    url('^$', views.index, name='index-view'),
]
