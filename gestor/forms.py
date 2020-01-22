from django import forms

from .models import Coleccion, Items_Pedidos, Presentacion, Producto

class PedidosForm(forms.Form):
   coleccion = forms.ModelChoiceField(label="Colección",queryset=Coleccion.objects.all(),
                                      #widget = forms.Select(attrs = {'onchange' : "myFunction();"}))
                                      widget = forms.Select(attrs = {'onchange' : "disable_all();"}))
   
   
   def __init__(self, *args, **kwargs):
        super(PedidosForm, self).__init__(*args, **kwargs)
        colecciones_ids = Coleccion.objects.all().values_list('id',flat=True)

        for pk in colecciones_ids:
            this_queryset = Coleccion.objects.get(id=pk).productos.all()
            self.fields['coleccion' + str(pk)] = forms.ModelChoiceField(label="Producto",
                                                                        queryset=this_queryset,
                                                                        disabled=True)
            self.fields['coleccion' + str(pk)].widget.attrs.update({'class': 'coleccion_drop'})

        self.fields['presentacion'] = forms.ModelChoiceField(label="Presentación", queryset=Presentacion.objects.all())
        self.fields['cantidad'] = forms.IntegerField(label="Cantidad",min_value=1)

class BarriosForm(forms.Form):
   choices = [("Todos","Todos"), ("Balvanera","Balvanera"), ("Palermo","Palermo")]
   barrio = forms.ChoiceField(choices=choices)


