from django.urls import path
from . import views

urlpatterns = [
   path('', views.homepage, name='homepage'),
   path('clientes/', views.shop_list, name='shop_list'),

]
