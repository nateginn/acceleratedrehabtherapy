# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-11-12 05:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0008_auto_20191111_0557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointmentblock',
            name='img',
        ),
    ]
