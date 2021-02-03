from .models import Ingrediente, Sandwich, Cliente, Pedido, PedidoSandwich, SandwichIngredientePedido
from django.forms import modelform_factory
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from datetime import datetime
from .forms import FechaForm, SandwichForm, IngredienteForm
from django.db import models

ClienteForm = modelform_factory(Cliente, exclude=[])


""" Pantalla inicial """
def index(request):
    
    if request.method == "POST":
        formaCliente = ClienteForm(request.POST)
        if formaCliente.is_valid():
            formaCliente.save()
            pedido = Pedido(fecha = datetime.now(), cliente = formaCliente.instance)
            pedido.save()
            return redirect('menu', id = pedido.id)
        else:
            return render(request, 'tienda/index.html', {
            'Cliente': formaCliente})    
            
    else:
        formaCliente = ClienteForm()
        return render(request, 'tienda/index.html', {
        'Cliente': formaCliente})



""" Pantalla de pedido de sandwiches """
def menu(request,id):
    
    if request.method == 'POST':
        sandwiches = Sandwich.objects.all()
        itemS = request.POST.get('checks')
        sand = Sandwich.objects.get(tamaño = itemS)
        pedid = Pedido.objects.get(pk = id)
        idCliente = pedid.cliente.id
        return redirect('ingredientes', id = sand.id, idc = idCliente, idp = pedid.id) 
        
    else:
        sandwiches = Sandwich.objects.all()
        return render(request, 'tienda/menu.html', {
            'Sandwiches': sandwiches}) 
    
    
""" Pantalla de Ingredientes """    
def ingredientes(request, id, idc, idp):
    if request.method == 'POST':
        ingredientes = Ingrediente.objects.all()
        itemI = request.POST.getlist('check')
        sand = Sandwich.objects.get(pk = id)
        pedid = Pedido.objects.get(pk = idp)
        pedidSand = PedidoSandwich(sandwich = sand, pedido = pedid)
        pedidSand.save() 
        for i in (range(len(itemI))):
            ingre = Ingrediente.objects.get(nombre = itemI[i])
            ingrePedido = SandwichIngredientePedido(sandwich = sand, ingrediente = ingre, pedido = pedid)
            ingrePedido.save()
           
        
        
        return redirect('modal', idc = idc, idp = idp) 
        
    else:
        ingredientes = Ingrediente.objects.all()
        return render(request, 'tienda/ingredientes.html', {
            'Ingredientes': ingredientes}) 
     
 
     
""" Ventana Modal """
def modal(request, idc, idp):
    if request.GET.get('button') == 'button':
        return redirect('factura', id = idc)
           
    elif request.GET.get('atras') == 'atras':
        return redirect('menu', id = idp) 
    
    else:
        return render(request, 'tienda/modal.html') 
        
    
    
""" Resumen de Pedido """    
    
def factura(request, id): 
    precioT = 0
    cliente = Cliente.objects.get(pk = id)
    pedido = Pedido.objects.get(cliente = cliente)
    pedidoSand = list(PedidoSandwich.objects.filter(pedido = pedido))
    pedidoIngre = list(SandwichIngredientePedido.objects.filter(pedido = pedido))
    sandwiches = Sandwich.objects.all()
    ingres = Ingrediente.objects.all()
    for i in range(len(pedidoIngre)):
        for m in range(len(ingres)):
            if pedidoIngre[i].ingrediente == ingres[m] and pedidoIngre[i].pedido == pedido:
                precioT = precioT + ingres[m].precio
    
    for j in range(len(pedidoSand)):
        for k in range(len(sandwiches)):
            if pedidoSand[j].sandwich == sandwiches[k] and pedidoSand[j].pedido == pedido:
                precioT = precioT + sandwiches[k].precio
                 
    
    return render(request, 'tienda/factura.html', {
        'Cliente': cliente, 'Pedidos': pedido,
        'PedidoSandwiche': pedidoSand, 'PedidoIngre': pedidoIngre,
        'PrecioT': precioT, 'Sandwiche': sandwiches, 'Ingredientes': ingres}) 
    

fechaF = FechaForm(use_required_attribute=False)
tamañoF = SandwichForm(use_required_attribute=False)
clienteF = ClienteForm(use_required_attribute=False)
ingredienteF = IngredienteForm(use_required_attribute=False)

""" Pantalla de reportes """    
def ventas(request):
    
    if request.method == 'POST':
        fechaF = FechaForm(request.POST)
        tamañoF = SandwichForm(request.POST)
        clienteF = ClienteForm(request.POST)
        ingredienteF = IngredienteForm(request.POST)
        
        """ reporte de ventas General """
        if not fechaF.data['fecha'] and not tamañoF.data['tamaño'] and not clienteF.data['nombre'] and not ingredienteF.data['ingrediente']:
            cliente = Cliente.objects.all()
            pedido = Pedido.objects.all()
            pedidoSand = PedidoSandwich.objects.all()
            sandwiches = Sandwich.objects.all()
            pedidoIngre = SandwichIngredientePedido.objects.all()
            ingredientes = Ingrediente.objects.all()         
        
            return render(request, 'tienda/ventas.html', {
                'Boton': 'no mostrar',
                'Venta': 'Generales',
                'Clientes': cliente,
                'Pedidos': pedido,
                'PedidoSand': pedidoSand,
                'Sandwiches': sandwiches,
                'Ingredientes': ingredientes,
                'PedidoIngre': pedidoIngre,
            })
        
        """ Reporte de ventas filtrado por fecha """ 
           
        if fechaF.data['fecha']:
            pedido = Pedido.objects.filter(fecha = fechaF.data['fecha'])
            cliente = Cliente.objects.all()
            pedidoSand = PedidoSandwich.objects.all()
            sandwiches = Sandwich.objects.all()
            ingredientes = Ingrediente.objects.all()
            pedidoIngre = SandwichIngredientePedido.objects.all() 
            clientes = []
            pedidoS = []
            pedidoI = []
            for i in range(len(pedido)):
                for j in range(len(cliente)):
                    if pedido[i].cliente == cliente[j]:
                        clientes.append(cliente[j])
             
            for i in range(len(pedido)):
                for j in range(len(pedidoSand)):
                    if pedido[i] == pedidoSand[j].pedido:
                       pedidoS.append(pedidoSand[j])
                       
            for i in range(len(pedido)):
                for j in range(len(pedidoIngre)):
                    if pedido[i] == pedidoIngre[j].pedido:
                       pedidoI.append(pedidoIngre[j])

            return render(request, 'tienda/ventas.html', {
                'Boton': 'no mostrar',
                'Venta': 'por Fecha',
                'Clientes': clientes,
                'Pedidos': pedido,
                'PedidoSand': pedidoS,
                'Sandwiches': sandwiches,
                'Ingredientes': ingredientes,
                'PedidoIngre': pedidoI,
            })
        
        """ Reporte de ventas por tamaño de sandwiche """    
           
        if tamañoF.data['tamaño']:
            sandwiche = Sandwich.objects.get(tamaño = tamañoF.data['tamaño'])
            pedido = Pedido.objects.all()
            cliente = Cliente.objects.all()
            pedidoSand = PedidoSandwich.objects.all()
            ingredientes = Ingrediente.objects.all()
            pedidoIngre = SandwichIngredientePedido.objects.all() 
            clientes = []
            pedidoS = []
            pedidoI = []
            pedidos = []
            sandwiches = []
            
            for i in range(len(pedidoSand)):
                if pedidoSand[i].sandwich == sandwiche:
                    pedidoS.append(pedidoSand[i])
                    
            for i in range(len(pedidoIngre)):
                if  sandwiche == pedidoIngre[i].sandwich:
                    pedidoI.append(pedidoIngre[i])
             
            for i in range(len(pedidoS)):
                for j in range(len(pedido)):
                    if pedidoS[i].pedido == pedido[j]:
                       pedidos.append(pedido[j])
                       
                       
            for i in range(len(pedidos)):
                for j in range(len(cliente)):
                    if pedidos[i].cliente == cliente[j]: 
                       clientes.append(cliente[j])
                       
            sandwiches.append(sandwiche)

            return render(request, 'tienda/ventas.html', {
                'Boton': 'no mostrar',
                'Venta': 'por Sandwich',
                'Clientes': clientes,
                'Pedidos': pedidos,
                'PedidoSand': pedidoS,
                'Sandwiches': sandwiches,
                'Ingredientes': ingredientes,
                'PedidoIngre': pedidoI,
            })
           
        """ Reporte de ventas por cliente """
        
        if clienteF.data['nombre']:
            cliente = Cliente.objects.get(nombre = clienteF.data['nombre'])
            sandwiches = Sandwich.objects.all()
            pedido = Pedido.objects.all()
            pedidoSand = PedidoSandwich.objects.all()
            ingredientes = Ingrediente.objects.all()
            pedidoIngre = SandwichIngredientePedido.objects.all() 
            pedidoS = []
            pedidoI = []
            pedidos = []
            clientes = []
            
            for i in range(len(pedido)):
                if pedido[i].cliente == cliente:
                    pedidos.append(pedido[i])
            
            for i in range(len(pedidos)):        
                for j in range(len(pedidoIngre)):
                    if pedidos[i] == pedidoIngre[j].pedido:
                        pedidoI.append(pedidoIngre[j])
             
            for i in range(len(pedidos)):
                for j in range(len(pedidoSand)):
                    if pedidos[i] == pedidoSand[j].pedido:
                       pedidoS.append(pedidoSand[j])
                       
            clientes.append(cliente)

            return render(request, 'tienda/ventas.html', {
                'Boton': 'no mostrar',
                'Venta': 'por Cliente',
                'Clientes': clientes,
                'Pedidos': pedidos,
                'PedidoSand': pedidoS,
                'Sandwiches': sandwiches,
                'Ingredientes': ingredientes,
                'PedidoIngre': pedidoI,
            })
            
        """ Reporte de ventas por ingrediente """
        
        if ingredienteF.data['ingrediente']:
            ingrediente = Ingrediente.objects.get(nombre = ingredienteF.data['ingrediente'])
            pedido = Pedido.objects.all()
            sandwiches = Sandwich.objects.all()
            cliente = Cliente.objects.all()
            pedidoSand = PedidoSandwich.objects.all()
            pedidosIn = SandwichIngredientePedido.objects.all()
            ingredientes = Ingrediente.objects.all()
            pedidoIngre = []
            pedidoS = []
            pedidoI = []
            pedidos = []
            clientes = []
            sandwiche = []
            ingredient = []
            
            for i in range(len(pedidosIn)):
                if(ingrediente == pedidosIn[i].ingrediente):
                    pedidoIngre.append(pedidosIn[i])
                    
            for i in range(len(pedidoIngre)):
                for j in range(len(pedido)):
                    if(pedidoIngre[i].pedido == pedido[j]):
                        pedidos.append(pedido[j])
                        
            for i in range(len(pedidos)):
                for j in range(len(cliente)):
                    if(pedidos[i].cliente == cliente[j]):
                        clientes.append(cliente[j])
            
            for i in range(len(pedidos)):
                for j in range(len(pedidoSand)):
                    if(pedidos[i] == pedidoSand[j].pedido):
                        pedidoS.append(pedidoSand[j])
                        
            for i in range(len(pedidoIngre)):
                for j in range(len(sandwiches)):
                    if(pedidoIngre[i].sandwich == sandwiches[j]):
                        sandwiche.append(sandwiches[j])
                        
            ingredient.append(ingrediente)
                              
                       
            return render(request, 'tienda/ventas.html', {
                'Boton': 'no mostrar',
                'Venta': 'por Ingrediente',
                'Clientes': clientes,
                'Pedidos': pedidos,
                'PedidoSand': pedidoS,
                'Sandwiches': sandwiche,
                'Ingredientes': ingredientes,
                'PedidoIngre': pedidoIngre,
            })
            
    else:
        fechaF = FechaForm(use_required_attribute=False)
        tamañoF = SandwichForm(use_required_attribute=False)
        clienteF = ClienteForm(use_required_attribute=False)
        ingredienteF = IngredienteForm(use_required_attribute=False)
        return render(request, 'tienda/ventas.html', {
            'Boton': 'mostrar',
            'Fecha': fechaF,
            'Tamaño': tamañoF,
            'Cliente': clienteF,
            'Ingrediente': ingredienteF
        })    