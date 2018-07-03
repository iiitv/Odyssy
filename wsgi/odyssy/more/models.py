from basic import utils

from django.db import models


class Talk(models.Model):
    def __str__(self):
        return str(self.title)

    @staticmethod
    def get_all_talks():
        """ Get all the announcements """
        return Talk.objects.all().order_by('-start_date')

    @staticmethod
    def get_latest_talks(cnt):
        """ get latest announcement """
        return Talk.objects.filter(
            utils.get_active_filter()
            ).order_by('-start_date')[:cnt]

    def get_start_date(self):
        return self.start_date.date()

    start_date = models.DateTimeField(default=utils.get_today_start)
    title = models.CharField(max_length=10000)
    speaker = models.TextField(max_length=5000, null=True, blank=True)
    description = models.TextField(max_length=90000, null=True, blank=True)
