# Generated by Django 3.2.9 on 2021-11-30 23:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='contenido',
            field=ckeditor.fields.RichTextField(default=True),
            preserve_default=False,
        ),
    ]