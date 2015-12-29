# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 02:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0014_auto_20151227_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='valid_end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 26, 2, 57, 27, 198285, tzinfo=utc)),
        ),
        migrations.AlterUniqueTogether(
            name='classlist',
            unique_together=set([('course', 'semester')]),
        ),
    ]