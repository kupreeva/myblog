# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_auto_20160319_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]