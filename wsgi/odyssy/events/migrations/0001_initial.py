# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-23 10:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'Sample Name', max_length=30)),
                ('start_time', models.DateTimeField(default=datetime.datetime.now)),
                ('end_time', models.DateTimeField(default=datetime.datetime.now)),
                ('description', models.TextField(max_length=20000)),
                ('place', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
        ),
    ]
