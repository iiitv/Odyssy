from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Announcement(models.Model):
    """ Model for Announcement
    key         -- Primary Key
    initDate    -- Initialization Date
    finDate     -- Final Date
    title       -- Title of the Announcement
    description -- Description of the Announcement
    """

    def __str__(self):
        return "#" + str(self.key) + " " + self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.finDate > self.initDate:
            super(Announcement, self).save()
        else:
            raise ValidationError("Final Date is smaller than initial Date")

    key = models.AutoField(primary_key=True)
    initDate = models.DateTimeField()
    finDate = models.DateTimeField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
