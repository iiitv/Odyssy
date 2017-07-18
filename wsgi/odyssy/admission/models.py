from django.db import models


class Admission(models.Model):
    """Model of Admission app
    fee_structure -- latest image of fee
    """
    fee_structure = models.ImageField(upload_to='fee_structure/')
