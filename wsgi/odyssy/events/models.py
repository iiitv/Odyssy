import calendar

import datetime
from django.db import models


class Event(models.Model):
    start_time = models.DateTimeField(default=datetime.datetime.now())
    end_time = models.DateTimeField(default=datetime.datetime.now())
    description = models.CharField(max_length=300)
    place = models.CharField(max_length=50)

    def __str__(self):
        return self.description + " at " + self.place + " on " + \
               str(self.start_time.day) + " - " + calendar.month_abbr[self.start_time.month] + \
               " - " + str(self.start_time.year)
