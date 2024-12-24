# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-30 19:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingvote',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='ratingvote',
            name='ip',
            field=models.GenericIPAddressField(db_index=True, verbose_name='ip'),
        ),
    ]
