from __future__ import unicode_literals

import itertools

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
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
    name = models.CharField(max_length=500, blank=True, null=True)
    slug = models.SlugField(max_length=1000, unique=True, blank=True, null=True)
    photo = models.ImageField(upload_to='people_images/', blank=True, null=True)
    post = models.CharField(max_length=2000, blank=True, null=True)
    tags = TaggableManager(blank=True)
    academic_highlights = models.CharField(
        max_length=20000, blank=True, null=True)
    institute = models.CharField(max_length=5000, blank=True, null=True)
    area_of_interest = models.CharField(max_length=50000, blank=True, null=True)
    office = models.CharField(max_length=10000, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(
        max_length=16, choices=STATUS_CHOICES, default='staff', blank=True, null=True)
    # Description page
    academic_qualifications = models.TextField(
        max_length=300000, blank=True, null=True)
    professional_memberships = models.TextField(
        max_length=300000, blank=True, null=True)
    work_experience = models.TextField(max_length=50000, blank=True, null=True)
    administrative_experience = models.TextField(
        max_length=20000, blank=True, null=True)
    publications = models.TextField(max_length=300000, blank=True, null=True)
    teaching = models.TextField(max_length=20000, blank=True, null=True)
    other = models.TextField(max_length=20000, blank=True, null=True)
    link_fb = models.URLField(blank=True, null=True, max_length=400)
    link_tw = models.URLField(blank=True, null=True, max_length=400)
    link_ln = models.URLField(blank=True, null=True, max_length=400)
    link_gs = models.URLField(blank=True, null=True, max_length=400)
    link_gh = models.URLField(blank=True, null=True, max_length=400)

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
        new_people = People.objects.create(user=instance)
        if not new_people.user.get_full_name():
            new_people.slug = orig = slugify(new_people.user.username)
        else:
            new_people.slug = orig = slugify(new_people.user.get_full_name())

        for x in itertools.count(1):
            if not People.objects.filter(slug=new_people.slug).exists():
                break
            new_people.slug = '%s-%d' % (orig, x)

        new_people.save()


@receiver(post_save, sender=User)
def save_user_people(sender, instance, **kwargs):
    instance.people.save()
