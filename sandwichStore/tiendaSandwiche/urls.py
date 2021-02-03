from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('menu/<int:id>', views.menu, name = 'menu'),
    path('ingredientes/<int:id>/<int:idc>/<int:idp>', views.ingredientes, name = 'ingredientes'),
    path('modal/<int:idc>/<int:idp>', views.modal, name= 'modal'),
    path('factura/<int:id>', views.factura, name = 'factura'),
    path('ventas/', views.ventas, name= 'ventas')
]   