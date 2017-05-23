from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class News(models.Model):
    """ Model of News app
    start_date - Start Date of News
    end_date - End Date of News
    title - Title for News
    description - Description of News
    """
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return str(self.pk) + ': ' + str(self.title)

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError('Start date has to be before End date')
