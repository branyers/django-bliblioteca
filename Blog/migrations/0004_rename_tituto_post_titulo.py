# Generated by Django 3.2.9 on 2021-12-01 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_post_contenido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tituto',
            new_name='titulo',
        ),
    ]
