# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-12-17 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_networks', '0008_auto_20190405_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sociallink',
            name='provider',
            field=models.CharField(choices=[('facebook', 'Facebook'), ('instagram', 'Instagram'), ('linkedin', 'LinkedIn'), ('twitter', 'Twitter'), ('youtube', 'YouTube')], max_length=16, unique=True, verbose_name='provider'),
        ),
    ]
