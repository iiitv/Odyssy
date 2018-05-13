from __future__ import unicode_literals
from django.core.exceptions import ValidationError

from django.db import models


class Committee(models.Model):
    """Model of Institute app
    name -- Name of the committee member
    post -- Post of the person in committee
    origin -- The origin committee of committee member
    """
    class Meta:
        ordering = ('name',)
        verbose_name = 'Committee'
        verbose_name_plural = 'Committees'

    COMMITTEE_CHOICES = [
        ('default', 'Select choice'),
        ('finance', 'Finance Committee'),
        ('building-works', 'Building And Works Committee'),
        ('hr-planning', 'HR Planning Committee'),
        ('research-council', 'Research Council'),
        ('strategic-planning', 'Strategic Planning Committee')
    ]
    POST_CHOICES = [
        ('default', 'Select choice'),
        ('Chairman', 'Chairman'),
        ('Vice Chairman', 'Vice Chairman'),
        ('Member', 'Member'),
        ('Member Secretary', 'Member Secretary'),
    ]
    name = models.CharField(max_length=50)
    post = models.CharField(
        max_length=20, choices=POST_CHOICES, default='default')
    origin = models.CharField(max_length=150)
    committee = models.CharField(
        max_length=30, choices=COMMITTEE_CHOICES, default='default')

    def __str__(self):
        return str(self.name) + ': ' + str(self.post) + ', ' + str(self.origin)

    def clean(self):
        if self.name is '':
            raise ValidationError('Name cannot be empty')
        elif self.post is '':
            raise ValidationError('Post cannot be empty')
        elif self.origin is '':
            raise ValidationError('Origin cannot be empty')
