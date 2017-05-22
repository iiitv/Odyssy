# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-20 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('key', models.IntegerField(primary_key=True, serialize=False)),
                ('initDate', models.DateTimeField()),
                ('finDate', models.DateTimeField()),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
