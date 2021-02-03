
# Factura
def factura(_tamaño,_precio,_totalI,_contS,_totalF):
    _opcionM = ''
    
    '_totalO = _totalO + _sand.get_precio() + _total'
    print()
    print("Subtotal a pagar por un sandwich " + str(_tamaño + ":" + str(_precio + _totalI)))
    print(30*"*")
    _opcionM = input("¿Desea Continuar [s/n]?: ")
    print(30*"*")
    
    if(_opcionM == 'n'): #En caso de que el usuario no quiera hacer otro pedido el sistema se despide
        print("El pedido tiene un total de " + str(_contS) + " sandwich(es) por un monto de " + str(_totalF))
        print("Gracias por su compra, regrese pronto")
        return _opcionM
    else:
        return _opcionM