from django.db import models
from django.db.models.expressions import F


class Admission(models.Model):
    """Model of Admission app
    fee_structure -- latest image of fee
    batch -- fee structure of that batch
    """
    STATUS_CHOICES = (
        ('btech', 'btech'),
        ('mtech', 'mtech'),
    )

    fee_structure = models.ImageField(upload_to='fee_structure/')
    batch = models.IntegerField(blank=True, null=True)
    programme = models.CharField(max_length=16, choices=STATUS_CHOICES, default='btech', blank=True, null=True)

    def __str__(self):
        return str(self.batch)

    def display_year(self):
        return str(self.batch) + '-' + str(F(self.batch)+1)

    @staticmethod
    def fetch_structures(programme):
        return Admission.objects.all().filter(programme=programme).order_by('-batch')[:4]
