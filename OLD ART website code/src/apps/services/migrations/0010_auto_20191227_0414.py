# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-12-27 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_auto_20191227_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(help_text='for seo, preview and breadcrumbs', max_length=128, verbose_name='Title'),
        ),
    ]
