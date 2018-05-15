from __future__ import unicode_literals

from django.db import models


class Semester(models.Model):
    class Meta:
        ordering = ('sem', )
        verbose_name = 'Semester'
        verbose_name_plural = 'Semesters'

    sem = models.PositiveIntegerField(default=1)
    structure_btech_it = models.TextField(max_length=20000, blank=True, null=True)
    structure_btech_cs = models.TextField(max_length=20000, blank=True, null=True)
    structure_mtech_cs = models.TextField(max_length=20000, blank=True, null=True)

    def __str__(self):
        return str(self.sem)


class Course(models.Model):
    class Meta:
        ordering = ('code', )
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    PROGRAMME_CHOICES = (
        ('btech', 'Bachelor of Technology'),
        ('mtech', 'Master of Technology'),
    )
    BRANCH_CHOICES = (
        ('cse', 'Computer Science & Engineering'),
        ('it', 'Information Technology'),
        ('both', 'Computer Science & Engineering and Information Technology'),
    )
    programme = models.CharField(max_length=120, choices=PROGRAMME_CHOICES, default='btech')
    branch = models.CharField(max_length=120, choices=BRANCH_CHOICES, default='cse')
    name = models.CharField(max_length=120, blank=True, null=True)
    code = models.CharField(max_length=6, unique=True)
    is_elective = models.BooleanField(default=False)
    # Lecture credits
    lecture = models.IntegerField(default=0)
    # Tutorial credits
    tutorial = models.IntegerField(default=0)
    # Practical credits
    practical = models.IntegerField(default=0)
    # Credits
    credits = models.IntegerField(default=0)
    content = models.TextField(max_length=10000, blank=True, null=True)
    text_book = models.TextField(max_length=120, blank=True, null=True)
    ref_book = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.code + ' : ' + self.name


class CourseInSem(models.Model):
    class Meta:
        ordering = ('semester', )
        verbose_name = 'CourseInSem'
        verbose_name_plural = 'CoursesInSems'

    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    semester = models.ForeignKey(Semester, on_delete=models.PROTECT)

    def __str__(self):
        return self.semester.__str__() + ' : ' + self.course.__str__()
