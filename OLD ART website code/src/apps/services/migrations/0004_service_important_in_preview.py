# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-11-14 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20191114_0427'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='important_in_preview',
            field=models.BooleanField(default=False, verbose_name='important in preview'),
        ),
    ]
