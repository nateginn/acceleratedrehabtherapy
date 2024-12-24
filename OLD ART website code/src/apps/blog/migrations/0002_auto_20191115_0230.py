# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-11-15 09:30
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogconfig',
            name='text_bottom',
            field=ckeditor.fields.CKEditorUploadField(blank=True, help_text='Image sizes: from <b>780x440</b> to <b>1024x578</b>', verbose_name='Content bottom'),
        ),
        migrations.AlterField(
            model_name='blogconfig',
            name='text_top',
            field=ckeditor.fields.CKEditorUploadField(blank=True, help_text='Image sizes: from <b>780x440</b> to <b>1024x578</b>', verbose_name='Content top'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='text_bottom',
            field=ckeditor.fields.CKEditorUploadField(blank=True, help_text='Image sizes: from <b>780x440</b> to <b>1024x578</b>', verbose_name='Content bottom'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='text_top',
            field=ckeditor.fields.CKEditorUploadField(blank=True, help_text='Image sizes: from <b>780x440</b> to <b>1024x578</b>', verbose_name='Content top'),
        ),
    ]
