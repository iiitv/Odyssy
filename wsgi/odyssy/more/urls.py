from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^hostel/$', views.hostel, name='hostel'),
    url(r'^student_corner/$', views.student_corner, name='student-corner'),
    url(r'^library/$', views.library, name='library'),
    url(r'^invited_talks/$', views.invited_talks, name='invited-talks'),
    url(r'.html/$', views.view_institute, name='institute-html')
]