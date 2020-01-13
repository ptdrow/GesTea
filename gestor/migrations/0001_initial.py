# Generated by Django 2.2.9 on 2020-01-13 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=75)),
                ('direccion', models.CharField(max_length=50)),
                ('lat', models.DecimalField(decimal_places=7, max_digits=10)),
                ('long', models.DecimalField(decimal_places=7, max_digits=10)),
                ('barrio', models.CharField(max_length=25)),
                ('contactos', models.CharField(max_length=100)),
                ('instagram', models.CharField(max_length=15)),
                ('telefono_local', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('interacciones', models.CharField(max_length=200)),
                ('pedidos', models.CharField(max_length=200)),
                ('notas', models.TextField()),
            ],
        ),
    ]
