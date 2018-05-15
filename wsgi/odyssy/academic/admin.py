from django.contrib import admin
from .models import Programme, Semester, Course, CourseInSem

admin.site.register(Programme)
admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(CourseInSem)
