from django import forms

from .models import Coleccion, Items_Pedidos, Presentacion, Producto

class ItemForm(forms.ModelForm):
   
   class Meta:
      model = Items_Pedidos
      fields = ('coleccion', 'producto', 'presentacion', 'cantidad',)

class PedidosForm(forms.Form):
   coleccion = forms.ModelChoiceField(label="Colección",queryset=Coleccion.objects.all())
   producto = forms.ModelChoiceField(label="Producto",queryset=Producto.objects.all())
   presentacion = forms.ModelChoiceField(label="Presentación", queryset=Presentacion.objects.all())
   cantidad = forms.IntegerField(label="Cantidad",min_value=1)

