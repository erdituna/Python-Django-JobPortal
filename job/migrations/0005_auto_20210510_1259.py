# Generated by Django 3.1.7 on 2021-05-10 09:59

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
