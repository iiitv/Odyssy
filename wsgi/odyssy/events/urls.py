from django.conf.urls import url

import views

urlpatterns = [
    url(r'^(?P<event_id>[0-9]+)/$',
        views.event_detail, name='event-view-single'),
    url('^$', views.event, name='event-view'),
]
