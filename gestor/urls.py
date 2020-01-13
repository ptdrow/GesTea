from django.urls import path
from . import views

urlpatterns = [
   path('', views.homepage, name='homepage'),
   path('clientes/', views.shop_list, name='shop_list'),
   path('contact/<int:pk>/', views.contact_details, name='contact_details'),

]
