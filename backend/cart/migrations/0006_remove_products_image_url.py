# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 09:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20171122_0859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='image_url',
        ),
    ]
