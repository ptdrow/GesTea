from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=75)
    direccion = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=10, decimal_places=7)
    long = models.DecimalField(max_digits=10, decimal_places=7)
    barrio = models.CharField(max_length=25)
    contactos = models.CharField(max_length=100)
    instagram = models.CharField(max_length=15)
    telefono_local = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    interacciones = models.CharField(max_length=200)
    pedidos = models.CharField(max_length=200)
    notas = models.TextField()

class Contacto(models.Model):
    nombre = models.CharField(max_length=75)
    cliente = models.ForeignKey('Cliente', null=True, on_delete=models.SET_NULL)
    cargo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    instagram = models.CharField(max_length=15)
    interacciones = models.CharField(max_length=200)
    pedidos = models.CharField(max_length=200)
    notas = models.TextField()

