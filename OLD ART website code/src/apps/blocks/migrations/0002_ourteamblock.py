# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-11-11 09:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import libs.stdimage.fields
import libs.storages.media_storage


class Migration(migrations.Migration):

    dependencies = [
        ('attachable_blocks', '0005_auto_20190321_1020'),
        ('blocks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurTeamBlock',
            fields=[
                ('attachableblock_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='attachable_blocks.AttachableBlock')),
                ('header', models.CharField(blank=True, max_length=128, verbose_name='header')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('button_text', models.TextField(blank=True, max_length=64, verbose_name='Button text')),
                ('img', libs.stdimage.fields.StdImageField(aspects='normal', blank=True, min_dimensions=(590, 395), storage=libs.storages.media_storage.MediaStorage('blocks/our_team/img'), upload_to='', variations={'admin': {'crop': False, 'size': (300, 150)}, 'mobile': {'size': (295, 200)}, 'normal': {'size': (590, 395)}}, verbose_name='image')),
            ],
            options={
                'verbose_name': 'Our Team',
                'verbose_name_plural': 'Our Team',
            },
            bases=('attachable_blocks.attachableblock',),
        ),
    ]
