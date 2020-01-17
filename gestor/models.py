from django.db import models
from decimal import Decimal
from datetime import date

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
    notas = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre


class Coleccion(models.Model):
    nombre = models.CharField(max_length=30)
    presentaciones = models.ManyToManyField('Presentacion', related_name='colecciones')
        
    def __str__(self):
        return self.nombre


class Presentacion(models.Model):
    nombre = models.CharField(max_length=30)
    precio_mayorista = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    precio_sugerido = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=75)
    coleccion = models.ForeignKey('Coleccion', null=True, on_delete=models.SET_NULL, related_name="productos")
        
    def __str__(self):
        return self.nombre


class Items_Pedidos(models.Model):
   pedido = models.ForeignKey('Pedido',on_delete=models.CASCADE, related_name="items")
   coleccion = models.ForeignKey('Coleccion',null=True,on_delete=models.SET_NULL)
   producto = models.ForeignKey('Producto',null=True,on_delete=models.SET_NULL)
   presentacion = models.ForeignKey('Presentacion',null=True,on_delete=models.SET_NULL)
   cantidad = models.PositiveSmallIntegerField()
   total_price = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal('0.00'))
   
   def calc_price(self):
      self.total_price = Decimal(self.cantidad) * self.presentacion.precio_mayorista


class Pedido(models.Model):
   cliente = models.ForeignKey('Cliente', null=True, blank=True, on_delete=models.SET_NULL, related_name="pedidos")
   contacto = models.ForeignKey('Contacto', null=True, blank=True, on_delete=models.SET_NULL, related_name="pedidos")
   total_price = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal('0.00'))
   fecha_creacion = models.DateField(auto_now_add=True)
   fecha_entrega = models.DateField(null=True, blank=True)
   entregado = models.BooleanField(default=False)

   def calc_price(self):
      total = 0
      for item in list(self.items.all()):
         total += item.total_price

      self.total_price = total

   def entregar(self):
      self.fecha_entrega = date.today()
      self.entregado = True
      self.save()

   def desentregar(self):
      self.fecha_entrega = None
      self.entregado = False
      self.save()



