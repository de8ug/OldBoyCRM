# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 02:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0010_auto_20151218_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studyrecord',
            name='course_record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.CourseRecord', verbose_name='\u7b2c\u51e0\u5929\u8bfe\u7a0b'),
        ),
        migrations.AlterField(
            model_name='studyrecord',
            name='score',
            field=models.IntegerField(choices=[(100, b'A+'), (90, b'A'), (85, b'B+'), (80, b'B'), (70, b'B-'), (60, b'C+'), (50, b'C'), (40, b'C-'), (0, b'D'), (-1, b'N/A'), (-100, b'COPY')], default=-1, verbose_name='\u672c\u8282\u5f97\u5206'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='valid_end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 26, 2, 49, 11, 687852, tzinfo=utc)),
        ),
    ]