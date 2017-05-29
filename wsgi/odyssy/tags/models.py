from __future__ import unicode_literals

from django.db import models


class Tags(models.Model):
    """ Model representation for Tags """

    def __str__(self):
        return self.tag_name

    @staticmethod
    def get_all():
        return Tags.objects.all()

    tag_name = models.CharField(max_length=10)
