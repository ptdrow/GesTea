from django.shortcuts import render, get_object_or_404
from .models import Cliente
from .models import Contacto

def homepage(request):
   return render(request, 'homepage.html', {})

def shop_list(request):
   shops = Cliente.objects.all().order_by('barrio')
   return render(request, 'shops.html', {'shops': shops})

def contact_details(request, pk):
   contact = get_object_or_404(Contacto, pk=pk)
   return render(request, 'contact.html', {'contact': contact})


