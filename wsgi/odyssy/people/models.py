from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from taggit.managers import TaggableManager

from django.db import models


class People(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name = 'People'
        verbose_name_plural = 'People'

    STATUS_CHOICES = (
        ('faculty', 'Faculty'),
        ('former_faculty', 'Former Faculty'),
        ('visiting_faculty', 'Visiting Faculty'),
        ('staff', 'Staff'),
        ('phd', 'PhD Scholars'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='people_images/', blank=True, null=True)
    post = models.CharField(max_length=50, blank=True, null=True)
    tags = TaggableManager(blank=True)
    academic_highlights = models.CharField(
        max_length=200, blank=True, null=True)
    institute = models.CharField(max_length=50, blank=True, null=True)
    area_of_interest = models.CharField(max_length=500, blank=True, null=True)
    office = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(
        max_length=16, choices=STATUS_CHOICES, default='staff', blank=True, null=True)
    # Description page
    academic_qualifications = models.TextField(
        max_length=500, blank=True, null=True)
    professional_memberships = models.TextField(
        max_length=500, blank=True, null=True)
    work_experience = models.TextField(max_length=500, blank=True, null=True)
    administrative_experience = models.TextField(
        max_length=200, blank=True, null=True)
    publications = models.TextField(max_length=10000, blank=True, null=True)
    teaching = models.TextField(max_length=200, blank=True, null=True)
    other = models.TextField(max_length=200, blank=True, null=True)

    def get_url(self):
        return reverse('people:details', args=[self.slug])

    def __str__(self):
        return str(self.name)

    @staticmethod
    def get_people_sorted(tag):
        return People.objects.filter(tags__name=tag).order_by('name')


@receiver(post_save, sender=User)
def create_user_people(sender, instance, created, **kwargs):
    if created:
        People.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_people(sender, instance, **kwargs):
    instance.people.save()
