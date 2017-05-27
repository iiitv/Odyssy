from __future__ import unicode_literals

import basic
from datetime import datetime, time

from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Q


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
        """ Get all the announcements """
        return Announcement.objects.all().order_by('-initDate')

    @staticmethod
    def get_single_announcement(announcement_id):
        """ get a single announcement by announcement_id """
        return Announcement.objects.filter(key=announcement_id)

    @staticmethod
    def get_latest_announcements(cnt):
        """ get latest announcement """
        return Announcement.objects.filter(
            basic.utils.get_active_filter()
           ).order_by('-initDate')[:cnt]

    @staticmethod
    def get_current_date():
        """ set default as start of date """
        return datetime.combine(datetime.today(), time.min)

    @staticmethod
    def get_final_date():
        """ set end as undefined date """
        return datetime.combine(datetime.max, time.max)

    key = models.AutoField(primary_key=True)
    initDate = models.DateTimeField(default=get_current_date)
    finDate = models.DateTimeField(default=get_final_date)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
