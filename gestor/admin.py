from django.contrib import admin
from .models import Cliente, Contacto, Presentacion, Coleccion, Producto

admin.site.register(Cliente)
admin.site.register(Contacto)
admin.site.register(Presentacion)
admin.site.register(Coleccion)
admin.site.register(Producto)
