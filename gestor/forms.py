from django import forms

from .models import Coleccion, Items_Pedidos

class ItemForm(forms.ModelForm):
   
   class Meta:
      model = Items_Pedidos
      fields = ('coleccion', 'producto', 'presentacion', 'cantidad',)

class PedidosForm(forms.Form):
   coleccion = forms.ModelChoiceField(label="Colección",queryset=Coleccion.objects.all(),
                                     )

