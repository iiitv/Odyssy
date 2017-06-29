from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager

from django.db import models


class People(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name = 'People'
        verbose_name_plural = 'People'

    STATUS_CHOICES = (
        ('faculty', 'Faculty'),
        ('staff', 'Staff'),
        ('visiting_faculty', 'Visiting Faculty'),
        ('administrative', 'Administration'),
    )
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='people_images/')
    post = models.CharField(max_length=50)
    tags = TaggableManager()
    academic_highlights = models.CharField(max_length=200, blank=True, null=True)
    institute = models.CharField(max_length=50, blank=True, null=True)
    area_of_interest = models.CharField(max_length=500, blank=True, null=True)
    office = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=50)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='staff')
    # Description page
    academic_qualifications = models.TextField(max_length=500, blank=True, null=True)
    professional_memberships = models.TextField(max_length=500, blank=True, null=True)
    work_experience = models.TextField(max_length=500, blank=True, null=True)
    administrative_experience = models.TextField(max_length=200, blank=True, null=True)
    publications = models.TextField(max_length=10000, blank=True, null=True)
    teaching = models.TextField(max_length=200, blank=True, null=True)
    other = models.TextField(max_length=200, blank=True, null=True)

    def get_url(self):
        return reverse('people:details', args=[self.slug])

    def __str__(self):
        return self.name

    @staticmethod
    def get_people_sorted(tag):
        return People.objects.filter(tags__name=tag).order_by('name')
