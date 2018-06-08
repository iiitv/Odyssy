# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-25 23:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20180526_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='status',
            field=models.CharField(blank=True, choices=[('faculty', 'Faculty'), ('former_faculty', 'Former Faculty'), ('visiting_faculty', 'Visiting Faculty'), ('staff', 'Staff'), ('phd', 'PhD Scholars')], default='staff', max_length=16, null=True),
        ),
    ]