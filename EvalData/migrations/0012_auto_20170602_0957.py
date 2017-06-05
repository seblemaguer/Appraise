# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-02 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EvalData', '0011_auto_20170602_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='directassessmentresult',
            name='end_time',
            field=models.FloatField(default=0, help_text='(in seconds)', verbose_name='End time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='directassessmentresult',
            name='start_time',
            field=models.FloatField(default=0, help_text='(in seconds)', verbose_name='Start time'),
            preserve_default=False,
        ),
    ]