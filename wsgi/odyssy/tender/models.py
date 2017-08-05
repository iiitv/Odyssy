from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.core.exceptions import ValidationError
from taggit.managers import TaggableManager

class Tender(models.Model):
    """
    Model of Tender app
    tender -- pdf of tender
    start_date    -- Initialization Date
    end_date     -- Final Date
    title       -- Title cum Description of Tender
    """
    class Meta:
        verbose_name = 'Tender'
        verbose_name_plural = 'Tenders'

    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    tender = models.FileField(upload_to='tender/')
    tags = TaggableManager(blank=True)

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError('Start date has to be before End date')

    @staticmethod
    def get_all_tender():
        """ Get all the Tenders """
        return Tender.objects.all().order_by('-start_date')


def set_default_tag(sender, instance, **kwargs):
    if not instance.tags:
        post_save.disconnect(set_default_tag, sender=sender)
        instance.tags.add('tender')
        instance.save()
        post_save.connect(set_default_tag, sender=sender)

post_save.connect(set_default_tag, sender=Tender)
