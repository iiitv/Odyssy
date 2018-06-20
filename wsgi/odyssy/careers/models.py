from django.db import models
import datetime

from autoslug import AutoSlugField


class Career(models.Model):
    class Meta:
        ordering = ('-start_date',)
        verbose_name = 'Career'
        verbose_name_plural = 'Careers'

    title = models.CharField(max_length=10000, blank=True, null=True)
    start_date = models.DateTimeField(default=datetime.datetime.now)
    end_date = models.DateTimeField(default=datetime.datetime.now)
    description = models.TextField(max_length=20000)
    file = models.FileField(upload_to='careers/')
    slug = AutoSlugField(null=True, unique=True, populate_from='title')

    def __str__(self):
        return self.title

    def get_start_date(self):
        return self.start_date.date()

    def get_end_date(self):
        return self.end_date.date()
