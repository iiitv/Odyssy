from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Q
import datetime


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

    def clean(self):
        if self.initDate > self.finDate:
            raise ValidationError('Start date is after end date')

    @staticmethod
    def get_all_announcement():
        return Announcement.objects.all().order_by('-initDate')

    @staticmethod
    def get_single_announcement(announcement_id):
        return Announcement.objects.filter(key=announcement_id)

    @staticmethod
    def get_latest_announcements(cnt):
        return Announcement.objects.filter(
            Q(initDate__gte=datetime.date.today())|
            Q(finDate__gte=datetime.date.today())
            ).order_by('-initDate')[:cnt]


    key = models.AutoField(primary_key=True)
    initDate = models.DateTimeField()
    finDate = models.DateTimeField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
