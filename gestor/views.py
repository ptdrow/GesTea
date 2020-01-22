from django.shortcuts import render, get_object_or_404
from .models import Cliente, Coleccion, Contacto, Pedido, Presentacion, Producto, Items_Pedidos
from django.http import HttpResponse
from .forms import PedidosForm, BarriosForm
from decimal import Decimal


def homepage(request):
   return render(request, 'homepage.html', {})

def shop_list(request):
   if request.method=="GET":
      shops = Cliente.objects.all().order_by('barrio')
   else:
      print(request.POST)
      barrio = request.POST.get('barrio')
      if barrio == 'Todos':
         shops = Cliente.objects.all().order_by('barrio')
      else:
         shops = Cliente.objects.filter(barrio=barrio).order_by('nombre')
   form = BarriosForm()
   return render(request, 'shops.html', {'form':form, 'shops': shops})

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
   if request.method=="POST":
      print(request.POST)
      
      entregados = list(Pedido.objects.filter(entregado=True).order_by('id').reverse().values_list('id', flat=True))
      marcados = request.POST.getlist("entregado")
      marcados = [int(item) for item in marcados]
            
      nuevos_entregados = [item for item in marcados if item not in entregados]
      desmarcados = [item for item in entregados if item not in marcados]
      
      for pk in nuevos_entregados:
         pedido = Pedido.objects.get(pk=pk)
         pedido.entregar()

      for pk in desmarcados:
         pedido = Pedido.objects.get(pk=pk)
         pedido.desentregar()

   pedidos = Pedido.objects.all().order_by('id').reverse()
   return render(request, 'pedidos_list.html', {'pedidos': pedidos})

def crear_pedido(request, pk):
   shop = get_object_or_404(Cliente, pk=pk)
   
   if request.method=="GET":
      pedido = Pedido(cliente=Cliente.objects.get(pk=pk))
      pedido.save()
   
   else:
      pedido_id = request.POST.get('pedido_id')
      pedido = Pedido.objects.get(pk=pedido_id)
      coleccion_id = request.POST.get('coleccion')
      coleccion = Coleccion.objects.get(pk=coleccion_id)
      producto_id = request.POST.get('coleccion'+str(coleccion_id))
      producto = Producto.objects.get(pk=producto_id)
      presentacion_id = request.POST.get('presentacion')
      presentacion = Presentacion.objects.get(pk=presentacion_id)
      cantidad = request.POST.get('cantidad')
      item = Items_Pedidos.objects.create(pedido=pedido, 
                                          coleccion=coleccion,
                                          producto=producto,
                                          presentacion=presentacion,
                                          cantidad=cantidad)
      item.calc_price()
      item.save()
      pedido.calc_price()
      pedido.save()
      
   form = PedidosForm()
   return render(request, 'crear_pedido.html', {'form': form, 'shop': shop, 'pedido':pedido})
   

