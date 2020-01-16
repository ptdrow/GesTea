from django.shortcuts import render, get_object_or_404
from .models import Cliente, Coleccion, Contacto, Pedido, Producto, Items_Pedidos
from django.http import HttpResponse
from .forms import PedidosForm
from decimal import Decimal


def homepage(request):
   return render(request, 'homepage.html', {})

def shop_list(request):
   shops = Cliente.objects.all().order_by('barrio')
   return render(request, 'shops.html', {'shops': shops})

def contact_details(request, pk):
   contact = get_object_or_404(Contacto, pk=pk)
   return render(request, 'contact.html', {'contact': contact})

def shop_details(request, pk):
   shop = get_object_or_404(Cliente, pk=pk)
   return render(request, 'shop_detail.html', {'shop': shop})

def product_list(request):
   products = Producto.objects.all().order_by('coleccion','nombre')
   return render(request, 'product_list.html', {'products': products})

def pedidos_list(request):
   pedidos = Pedido.objects.all().order_by('id').reverse()
   return render(request, 'pedidos_list.html', {'pedidos': pedidos})

def pedido_nuevo(request):
   return render(request, 'pedido_nuevo.html', {})

def crear_pedido(request, pk):
   shop = get_object_or_404(Cliente, pk=pk)
   
   if request.method=="GET":
      pedido = Pedido(cliente=Cliente.objects.get(pk=pk))
      pedido.save()
      print(pedido.pk)
   
   else:
      print(request.POST)
      pedido_id = request.POST.get('pedido_id')
      pedido = Pedido.objects.get(pk=pedido_id)
      coleccion_id = request.POST.get('coleccion')
      coleccion = Coleccion.objects.get(pk=coleccion_id)
      item = Items_Pedidos.objects.create(pedido=pedido, 
                                          coleccion=coleccion,
                                          cantidad=2,
                                          total_price=Decimal('12.00'))
      pedido.calc_price()
      pedido.save()
      
   form = PedidosForm()
   return render(request, 'crear_pedido.html', {'form': form, 'shop': shop, 'pedido':pedido})
   

