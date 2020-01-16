from django.urls import path
from . import views

urlpatterns = [
   path('', views.homepage, name='homepage'),
   path('clientes/', views.shop_list, name='shop_list'),
   path('contact/<int:pk>/', views.contact_details, name='contact_details'),
   path('pedidos/', views.pedidos_list, name='pedidos_list'),
   path('pedidos/new/', views.pedido_nuevo, name='pedido_nuevo'),
   path('productos/', views.product_list, name='product_list'),
   path('shop/<int:pk>/pedido', views.crear_pedido, name='crear_pedido'),
   path('shop/<int:pk>/', views.shop_details, name='shop_details'),
]
