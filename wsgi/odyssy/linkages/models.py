from __future__ import unicode_literals

from django.db import models
from django.shortcuts import get_object_or_404


class Linkages(models.Model):
    """Model of the Linkages App

    """
    class Meta:
        verbose_name = 'Linkage'
        verbose_name_plural = 'Linkages'

    name = models.CharField(max_length=300, blank=True, null=True)
    short_name = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(max_length=300, blank=True, null=True)
    description = models.TextField(max_length=10000, blank=True, null=True)
    logo = models.ImageField(upload_to='linkage_images/', blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self):
        return str(self.name)

    @staticmethod
    def get_all_linkages():
        links = Linkages.objects.all()
        return links.order_by('name')

    @staticmethod
    def get_single_link(link_id):
        single_link = get_object_or_404(Linkages, pk=link_id)
        return single_link
