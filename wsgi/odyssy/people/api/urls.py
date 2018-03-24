from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^administration/$', views.AdministrationList.as_view(),
        name='api-administration'),
    url(r'^faculty/$', views.FacultyList.as_view(), name='api-faculty'),
    url(r'^visiting_faculty/$', views.VisitingFacultyList.as_view(),
        name='api-visiting_faculty'),
    url(r'^staff/$', views.StaffList.as_view(), name='api-staff'),
    url(r'^tag/(?P<tag>[-\w]+)/$',
        views.TaggedPeople.as_view(), name='api-filter_by_tag'),
    url(r'^(?P<slug>[-\w]+)/$', views.Details.as_view(), name='api-details')
]
