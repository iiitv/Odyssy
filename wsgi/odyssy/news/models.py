from basic import utils
from taggit.managers import TaggableManager

from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db import models
from django.shortcuts import get_object_or_404
from django.db.models.signals import post_save


class News(models.Model):
    """ Model of News app.

    start_date -- Start Date of News
    end_date -- End Date of News
    title -- Title for News
    description -- Description of News
    """
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=50)
    tags = TaggableManager(blank=True)
    description = models.TextField(max_length=500)

    def __str__(self):
        return str(self.pk) + ': ' + str(self.title)

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError('Start date has to be before End date')

    @staticmethod
    def get_all_news():
        return News.objects.order_by('-start_date')

    @staticmethod
    def get_latest_news(num_items):
        return News.objects.filter(
            utils.get_active_filter()
        ).order_by('-start_date')[:num_items]

    @staticmethod
    def get_single_news_detail(event_id):
        single_news = get_object_or_404(News, pk=event_id)
        return single_news

    @staticmethod
    def get_news_tag(tag_name):
        return News.objects.filter(tags__name=tag_name).order_by('-start_date')

    @staticmethod
    def get_latest_news_tag(tag_name, cnt):
        return News.objects.filter(
            utils.get_active_filter()
        ).filter(tags__name=tag_name).order_by('-start_date')[:cnt]

    @staticmethod
    def get_model_type():
        return "News"


def set_default_tag(sender, instance, **kwargs):
    if not instance.tags:
        post_save.disconnect(set_default_tag, sender=sender)
        instance.tags.add('news')
        instance.save()
        post_save.connect(set_default_tag, sender=sender)

post_save.connect(set_default_tag, sender=News)
