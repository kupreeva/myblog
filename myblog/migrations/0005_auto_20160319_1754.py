# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_auto_20160319_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
