# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ue', '0002_auto_20170207_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='yolo',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
    ]