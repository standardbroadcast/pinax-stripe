# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinax_stripe', '0015_merge_20171030_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='authorized',
            field=models.BooleanField(default=True),
        ),
    ]
