from django.contrib import admin

from .models import Pedido, Cliente, Sandwich, Ingrediente, PedidoSandwich, SandwichIngredientePedido

admin.site.register(Pedido)
admin.site.register(Cliente)
admin.site.register(Sandwich)
admin.site.register(Ingrediente)
admin.site.register(PedidoSandwich)
admin.site.register(SandwichIngredientePedido)





