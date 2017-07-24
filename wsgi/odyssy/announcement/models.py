from basic import utils
from taggit.managers import TaggableManager

from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save


class Announcement(models.Model):
    """ Model for Announcement
    key         -- Primary Key
    start_date    -- Initialization Date
    end_date     -- Final Date
    title       -- Title of the Announcement
    description -- Description of the Announcement
    """

    def __str__(self):
        return "#" + str(self.key) + " " + str(self.title)

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
        return Announcement.objects.filter(tags__name=tag_name).order_by('-start_date')

    @staticmethod
    def get_latest_announcement_tag(tag_name, cnt):
        return Announcement.objects.filter(
            utils.get_active_filter()
            ).filter(tags__name=tag_name).order_by('-start_date')[:cnt]

    @staticmethod
    def get_model_type():
        return "Announcement"

    key = models.AutoField(primary_key=True)
    start_date = models.DateTimeField(default=utils.get_today_start)
    end_date = models.DateTimeField(default=utils.get_today_end)
    tags = TaggableManager(blank=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)


def set_default_tag(sender, instance, **kwargs):
    if not instance.tags:
        post_save.disconnect(set_default_tag, sender=sender)
        instance.tags.add('announcement')
        instance.save()
        post_save.connect(set_default_tag, sender=sender)

post_save.connect(set_default_tag, sender=Announcement)
