# Generated by Django 2.2.9 on 2020-01-14 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0012_coleccion_presentaciones'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='presentaciones',
        ),
    ]
