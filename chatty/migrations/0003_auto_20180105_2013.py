# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-05 20:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatty', '0002_auto_20180105_2006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text3',
        ),
    ]