# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 21:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_auto_20160319_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='slug',
        ),
    ]