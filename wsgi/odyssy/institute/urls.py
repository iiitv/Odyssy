from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^building-works/$', views.view_building_works, name='building-works'),
    url(r'^finance/$', views.view_finance, name='finance'),
    url(r'^hr-planning/$', views.view_hr_planning, name='hr-planning'),
    url(r'^research-council/$', views.view_research_council, name='research-council'),
    url(r'^strategic-planning/$', views.view_strategic_planning,
        name='strategic-planning'),
    url(r'.html/$', views.view_institute, name='institute-html')
]
