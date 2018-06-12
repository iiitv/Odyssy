from __future__ import unicode_literals

import itertools

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify


class Calendar(models.Model):
    class Meta:
        ordering = ('-date', )
        verbose_name = 'Academic Calender'
        verbose_name_plural = 'Academic Calenders'

    file = models.FileField(upload_to='calenders/')
    slug = models.SlugField(unique=True, null=True, blank=True)
    name = models.TextField(max_length=1000, unique=True, blank=True, null=True, default='ac')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name + ' : ' + str(self.date)

    def get_url(self):
        return reverse('academic:down-calender', args=[self.slug])


@receiver(post_save, sender=Calendar)
def slugify_calender(sender, instance, created, **kwargs):
    if created:
        instance.slug = orig = slugify(instance.name)

        for x in itertools.count(1):
            if not Calendar.objects.filter(slug=instance.slug).exists():
                break
            instance.slug = '%s-%d' % (orig, x)

        instance.save()


class Programme(models.Model):
    class Meta:
        ordering = ('name', )
        verbose_name = 'Programme'
        verbose_name_plural = 'Programmes'

    name = models.CharField(max_length=50, blank=True, null=True, help_text='B.Tech, M.Tech or P.hD.')
    full_name = models.CharField(max_length=100, blank=True, null=True)
    branch_code = models.CharField(max_length=10, blank=True, null=True, help_text='e.g. CSE')
    branch_name = models.CharField(max_length=100, blank=True, null=True)
    info = models.TextField(max_length=5000, blank=True, null=True)

    def __str__(self):
        return str(self.name) + ' ' + str(self.branch_code)

    def get_url(self):
        return reverse('academic:single-programme', args=[self.name, self.branch_code])


class Course(models.Model):
    class Meta:
        ordering = ('code', )
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    SEM_CHOICES = (
        ('1', 'Semester I'),
        ('2', 'Semester II'),
        ('3', 'Semester III'),
        ('4', 'Semester IV'),
        ('5', 'Semester V'),
        ('6', 'Semester VI'),
        ('7', 'Semester VII'),
        ('8', 'Semester VII1')
    )
    programme = models.ForeignKey(Programme, on_delete=models.PROTECT)
    semester = models.CharField(max_length=120, choices=SEM_CHOICES, default='1')
    name = models.CharField(max_length=120, blank=True, null=True)
    code = models.CharField(max_length=6, unique=True, help_text='Unique code e.g. CSE101')
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

    def get_url(self):
        return reverse('academic:single-course', args=[self.programme.name, self.programme.branch_code, self.semester,
                                                       self.code])
