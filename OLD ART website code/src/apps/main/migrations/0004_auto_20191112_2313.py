# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-11-13 06:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20191112_0510'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mainpageconfig',
            options={'default_permissions': ('change',), 'verbose_name': 'settings'},
        ),
    ]
