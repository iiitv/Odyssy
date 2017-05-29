from basic import utils
from tags.models import Tags

from django.db import models
from django.core.exceptions import ValidationError


class Announcement(models.Model):
    """ Model for Announcement
    key         -- Primary Key
    start_date    -- Initialization Date
    end_date     -- Final Date
    title       -- Title of the Announcement
    description -- Description of the Announcement
    """

    def __str__(self):
        return "#" + str(self.key) + " " + self.title

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError('Start date is after end date')

    @staticmethod
    def get_all_announcement():
        """ Get all the announcements """
        return Announcement.objects.all().order_by('-start_date')

    @staticmethod
    def get_single_announcement(announcement_id):
        """ get a single announcement by announcement_id """
        return Announcement.objects.filter(key=announcement_id)

    @staticmethod
    def get_latest_announcements(cnt):
        """ get latest announcement """
        return Announcement.objects.filter(
            utils.get_active_filter()
            ).order_by('-start_date')[:cnt]

    @staticmethod
    def get_announcement_tag(tag_name):
        """ Fetches all announcements with tag """
        return Announcement.objects.filter(tags__tag_name=tag_name)

    key = models.AutoField(primary_key=True)
    start_date = models.DateTimeField(default=utils.get_today_start)
    end_date = models.DateTimeField(default=utils.get_today_end)
    tags = models.ManyToManyField(Tags)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
