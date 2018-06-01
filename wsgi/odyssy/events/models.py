import calendar

import datetime

from django.core.exceptions import ValidationError
from django.db import models
from django.shortcuts import get_object_or_404
from django.urls import reverse


class Event(models.Model):
    title = models.CharField(max_length=30, default="Sample Name")
    start_date = models.DateTimeField(default=datetime.datetime.now)
    end_date = models.DateTimeField(default=datetime.datetime.now)
    description = models.TextField(max_length=20000)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    place = models.CharField(max_length=100, null=True,
                             default=None, blank=True)

    def __str__(self):
        event_str = self.title + " on " + str(self.start_date.day) + \
            " - " + calendar.month_abbr[self.start_date.month] + \
            " - " + str(self.start_date.year)
        if self.place:
            event_str += " at " + self.place
        return event_str

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError("Start Date should be before end date")
        if self.place:
            self.place = self.place.strip(' \t\n')

    @staticmethod
    def get_all_events():
        return Event.objects.order_by('-start_date')

    @staticmethod
    def get_latest_events(num_items):
        events_list = Event.get_all_events()[:num_items]
        return events_list

    @staticmethod
    def get_single_event_detail(event_slug):
        single_event = get_object_or_404(Event, pk=event_slug)
        return single_event

    def get_url(self):
        return reverse('event:event-view-single', args=[self.slug])
