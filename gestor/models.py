from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=75)
    
    direccion = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    long = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    barrio = models.CharField(max_length=25)
    
    instagram = models.CharField(max_length=15, null=True, blank=True)
    telefono_local = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    
    interacciones = models.CharField(max_length=200, null=True, blank=True)
    pedidos = models.CharField(max_length=200, null=True, blank=True)
    notas = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre + " (" + self.barrio + ")"

class Contacto(models.Model):
    nombre = models.CharField(max_length=75)
    establecimiento = models.ForeignKey('Cliente', null=True, blank=True, on_delete=models.SET_NULL, related_name="contactos")
    cargo = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    instagram = models.CharField(max_length=15, null=True, blank=True)
    interacciones = models.CharField(max_length=200, null=True, blank=True)
    pedidos = models.CharField(max_length=200, null=True, blank=True)
    notas = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre

