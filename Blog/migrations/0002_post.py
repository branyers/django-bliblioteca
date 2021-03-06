# Generated by Django 3.2.9 on 2021-11-30 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tituto', models.CharField(max_length=100, verbose_name='Titulo')),
                ('slug', models.CharField(max_length=100, verbose_name='slug')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripcion')),
                ('imagen', models.URLField(max_length=300, verbose_name='Imagen')),
                ('estado', models.BooleanField(default=True, verbose_name='Publicado/No Publicado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='Blog.autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria', to='Blog.categoria')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'db_table': 'Post',
            },
        ),
    ]
