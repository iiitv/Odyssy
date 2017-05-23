import calendar

import datetime

from django.core.exceptions import ValidationError
from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=30, default="Sample Name")
    start_time = models.DateTimeField(default=datetime.datetime.now())
    end_time = models.DateTimeField(default=datetime.datetime.now())
    description = models.TextField(max_length=300)
    place = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " at " + self.place + " on " + \
               str(self.start_time.day) + " - " + calendar.month_abbr[self.start_time.month] + \
               " - " + str(self.start_time.year)

    def clean(self):
        if self.start_time > self.end_time:
            raise ValidationError("Start Date should be before end date")