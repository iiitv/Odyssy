from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Announcement(models.Model):
    """ Model for Announcement
    key         -- Primary Key
    initDate    -- Initialization Date
    finDate     -- Final Date
    title       -- Title of the Announcement
    description -- Description of the Announcement
    """
    key = models.AutoField(primary_key=True)
    initDate = models.DateTimeField()
    finDate = models.DateTimeField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
