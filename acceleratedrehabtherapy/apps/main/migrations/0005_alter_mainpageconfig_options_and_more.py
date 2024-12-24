# Generated by Django 5.1.4 on 2024-12-20 06:28

import django.utils.timezone
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_alter_mainpageconfig_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="mainpageconfig",
            options={
                "ordering": ["-created"],
                "verbose_name": "Page Content",
                "verbose_name_plural": "Page Contents",
            },
        ),
        migrations.RemoveField(
            model_name="mainpageconfig",
            name="button_text",
        ),
        migrations.AddField(
            model_name="mainpageconfig",
            name="created",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Created"
            ),
        ),
        migrations.AlterField(
            model_name="mainpageconfig",
            name="background",
            field=models.ImageField(
                blank=True,
                help_text="Recommended size: 1400x800 pixels",
                upload_to="backgrounds",
                verbose_name="Background",
            ),
        ),
        migrations.AlterField(
            model_name="mainpageconfig",
            name="text",
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name="Content"),
        ),
        migrations.AlterField(
            model_name="mainpageconfig",
            name="title",
            field=models.CharField(
                help_text="Page title", max_length=128, verbose_name="Title"
            ),
        ),
    ]
