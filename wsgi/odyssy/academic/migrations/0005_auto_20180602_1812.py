# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-02 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0004_auto_20180602_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.CharField(choices=[('1', 'Semester I'), ('2', 'Semester II'), ('3', 'Semester III'), ('4', 'Semester IV'), ('5', 'Semester V'), ('6', 'Semester VI'), ('7', 'Semester VII'), ('8', 'Semester VII1')], default='1', max_length=120),
        ),
    ]