from django.contrib import admin
from .models import Semester, Course, CourseInSem

admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(CourseInSem)
