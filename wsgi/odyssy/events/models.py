import calendar

import datetime

from django.core.exceptions import ValidationError
from django.db import models
from django.shortcuts import get_object_or_404


class Event(models.Model):
    name = models.CharField(max_length=30, default="Sample Name")
    start_time = models.DateTimeField(default=datetime.datetime.now())
    end_time = models.DateTimeField(default=datetime.datetime.now())
    description = models.TextField(max_length=300)
    place = models.CharField(max_length=50, null=True, default=None, blank=True)

    def __str__(self):
        event_str = self.name  + " on " + str(self.start_time.day) + \
            " - " + calendar.month_abbr[self.start_time.month] + \
            " - " + str(self.start_time.year)
        if self.place is not None:
            event_str = event_str + self.place
        return event_str

    def clean(self):
        if self.start_time > self.end_time:
            raise ValidationError("Start Date should be before end date")

    @staticmethod
    def get_all_events():
        return Event.objects.order_by('-start_time')

    @staticmethod
    def get_latest_events(num_items):
        events_list = Event.get_all_events()[:num_items]
        return events_list

    @staticmethod
    def get_single_event_detail(event_id):
            single_event = get_object_or_404(Event, pk=event_id)
            return single_event

