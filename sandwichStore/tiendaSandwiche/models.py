from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    
class Pedido(models.Model):
    fecha = models.DateField("Fecha Pedido")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
class Sandwich(models.Model):
    tamaño = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    
class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=3, decimal_places=1)

class PedidoSandwich(models.Model):
    sandwich = models.ForeignKey(Sandwich, default=None , on_delete=models.CASCADE, null=True)
    pedido = models.ForeignKey(Pedido, default=None , on_delete=models.CASCADE)
    
class SandwichIngredientePedido(models.Model):    
    sandwich = models.ForeignKey(Sandwich, default=None , on_delete=models.CASCADE, null=True)
    ingrediente = models.ForeignKey(Ingrediente, default=None , on_delete=models.CASCADE, null = True)
    pedido = models.ForeignKey(Pedido, default=None , on_delete=models.CASCADE)
    
