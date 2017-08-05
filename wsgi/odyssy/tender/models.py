from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from taggit.managers import TaggableManager

class Tender(models.Model):
    """Model of Tender app
    tender -- pdf of tender
    """

    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200)
    tender = models.FileField(upload_to='tender/', validators=[validate_file_extension])
    tags = TaggableManager()

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError('Start date has to be before End date')


def validate_file_extension(value):
    if not value.name.endswith('.pdf'):
       raise ValidationError(u'Invalid File Extension, Only PDFs are allowed.')