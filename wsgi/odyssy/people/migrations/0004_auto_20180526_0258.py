# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-25 21:28
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20180513_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
