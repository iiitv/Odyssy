from __future__ import unicode_literals

from django.db import models


class Tags(models.Model):
    """ Model representation for Tags
    tag_name : name of the tag
    """

    def __str__(self):
        return self.tag_name

    @staticmethod
    def get_all():
        """ Fetches all the tags """
        return Tags.objects.all()

    tag_name = models.CharField(max_length=10)
