# Generated by Django 2.2.9 on 2020-01-14 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0011_coleccion_presentacion_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='coleccion',
            name='presentaciones',
            field=models.ManyToManyField(related_name='colecciones', to='gestor.Presentacion'),
        ),
    ]
