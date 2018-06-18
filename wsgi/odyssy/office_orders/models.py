import datetime

from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save
from django.utils import timezone
from django.core.exceptions import ValidationError
from taggit.managers import TaggableManager


class OfficeOrders(models.Model):
    """
    Model of Office Order app
    order -- pdf of office order
    start_date    -- Initialization Date
    end_date     -- Final Date
    title       -- Title cum Description of Tender
    """
    class Meta:
        verbose_name = 'Office Order'
        verbose_name_plural = 'Office Orders'

    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    order = models.FileField(upload_to='office_order/')
    tags = TaggableManager(blank=True)

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError('Start date has to be before End date')

    def __str__(self):
        return str(self.title) + str(self.start_date) + '-' + str(self.end_date)

    @staticmethod
    def get_all_tender():
        """ Get all the Office Orders """
        return OfficeOrders.objects.all().order_by('-start_date')

    @staticmethod
    def get_all_active_orders():
        """
        Get all active office orders
        :return: Iterable containing all office orders
        """
        today = datetime.datetime.today()
        return OfficeOrders.objects.filter(start_date__lt=today, end_date__gt=today).order_by('-start_date')

    @staticmethod
    def get_archives():
        """
        Get all archived Office Orders
        :return: Iterable containing all archived office orders
        """
        today = datetime.datetime.today()
        return OfficeOrders.objects.all().exclude(start_date__lt=today, end_date__gt=today).order_by('-start_date')


def set_default_tag(sender, instance, **kwargs):
    if not instance.tags:
        post_save.disconnect(set_default_tag, sender=sender)
        instance.tags.add('office-order')
        instance.save()
        post_save.connect(set_default_tag, sender=sender)


post_save.connect(set_default_tag, sender=OfficeOrders)
