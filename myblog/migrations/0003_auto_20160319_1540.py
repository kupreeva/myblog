# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 15:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='like_data',
            new_name='created_at',
        ),
    ]