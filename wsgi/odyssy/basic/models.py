from __future__ import unicode_literals
from taggit.managers import TaggableManager
from photologue.models import Photo

from django.db import models


class PhotoExtended(models.Model):
    """ Tag based Model for Images """
    photo = models.OneToOneField(Photo, related_name='extended')
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.photo.title

    @staticmethod
    def get_photo_tag(tag_name):
        return PhotoExtended.objects.filter(tags__name=tag_name)

    @staticmethod
    def get_latest_images_tag(tag_name, cnt):
        return PhotoExtended.objects.filter(
            tags__name=tag_name
        ).order_by('-photo__date_added')[:cnt]
