from django.shortcuts import render
from .models import Cliente

def homepage(request):
   return render(request, 'homepage.html', {})

def shop_list(request):
   shops = Cliente.objects.all().order_by('barrio')
   return render(request, 'shops.html', {'shops': shops})


