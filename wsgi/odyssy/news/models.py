from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db import models
from django.shortcuts import get_object_or_404


class News(models.Model):
    """ Model of News app.

    start_date -- Start Date of News
    end_date -- End Date of News
    title -- Title for News
    description -- Description of News
    """
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

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
        news_list = News.get_all_news()[:num_items]
        return news_list

    @staticmethod
    def get_single_news_detail(event_id):
        single_news = get_object_or_404(News, pk=event_id)
        return single_news
