# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-11-12 09:16
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone
import libs.stdimage.fields
import libs.storages.media_storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='for seo, preview and breadcrumbs', max_length=128, verbose_name='Title')),
                ('header', models.TextField(max_length=255, verbose_name='Header')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('button_text', models.TextField(blank=True, max_length=64, verbose_name='Button text')),
                ('text_top', ckeditor.fields.CKEditorUploadField(blank=True, help_text='Image sizes: from <b>800x450</b> to <b>1024x576</b>', verbose_name='Content top')),
                ('text_bottom', ckeditor.fields.CKEditorUploadField(blank=True, help_text='Image sizes: from <b>800x450</b> to <b>1024x576</b>', verbose_name='Content bottom')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='change date')),
            ],
            options={
                'verbose_name': 'settings',
                'abstract': False,
                'default_permissions': ('change',),
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='for seo, preview and breadcrumbs', max_length=128, verbose_name='Title')),
                ('header', models.TextField(max_length=255, verbose_name='Header')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('button_text', models.TextField(blank=True, max_length=64, verbose_name='Button text')),
                ('text_top', ckeditor.fields.CKEditorUploadField(blank=True, help_text='Image sizes: from <b>800x450</b> to <b>1024x576</b>', verbose_name='Content top')),
                ('text_bottom', ckeditor.fields.CKEditorUploadField(blank=True, help_text='Image sizes: from <b>800x450</b> to <b>1024x576</b>', verbose_name='Content bottom')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='change date')),
                ('slug', models.SlugField(max_length=128, verbose_name='slug')),
                ('visible', models.BooleanField(default=True, verbose_name='visible')),
                ('sort_order', models.PositiveIntegerField(default=0, verbose_name='order')),
                ('note', models.TextField(blank=True, verbose_name='note')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='publication date')),
                ('status', models.IntegerField(choices=[(1, 'Draft'), (2, 'Public')], default=1, verbose_name='status')),
                ('img', libs.stdimage.fields.StdImageField(aspects=(), blank=True, min_dimensions=(380, 235), null=True, storage=libs.storages.media_storage.MediaStorage('std_page/img'), upload_to='', variations={'admin': {'crop': True, 'size': (270, 200)}, 'normal': {'crop': True, 'size': (380, 235)}}, verbose_name='img ')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ('-date', '-id'),
            },
        ),
    ]
