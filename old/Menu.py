from Factura import factura
from Ingrediente import Ingrediente
from Sandwiche import Sandwiche
import Factura as f 

# Metodo ingredients almacena los nombres de los ingredientes que pide el usuario
def ingredients(lista):
    """ Metodo ingredients almacena los nombres de los ingredientes que pide el usuario """
    ingredientes = ''
    
    for i in lista:
        if(i == lista[-1]):
            ingredientes += i 
        else:
            ingredientes += i + ', '
    
    return ingredientes

#Metodo menu el cual sirve para ejecutar todo el pedido del usuario

def menu():
    _opcion = ''
    _contS = 1
    _contI = 1
    _sand = ''
    _ingre = ''
    _listI = []
    _ingreN = ''
    _total = 0
    _opcionM = ''
    _totalF = 0
    
    #Ciclo de todo el menu 
    while (_opcionM != 'n'):
        _sand = Sandwiche()
        _ingreN = Ingrediente()
        print(30*"*")
        print("SANDWICHES UCAB")
        print("Sandwiche Número " + str(_contS))
        print(30*"*")
        print()
        
        #Pedido de sandwiches
        #Ciclo para el pedido de sandwiches   
        while (_opcion != "d") and (_opcion != "t") and (_opcion != "i"):    
            print("Opciones:")
            _opcion = input("Tamaños: Triple ( t ) Doble ( d ) Individual ( i ): ")
            if(_opcion == "d"):
                _sand = Sandwiche("Doble")
            elif(_opcion == "t"):
                _sand = Sandwiche("Triple")
            elif(_opcion == "i"):
                _sand = Sandwiche("Individual")
            else:
                print("Debe seleccionar el tamaño correcto!!")

        #Pedido de ingredientes
        print()
        print("Ingredientes:")
        print("Jamón" + 25*" " + "(ja)")
        print("Champiñones" + 19*" " + "(ch)")
        print("Pimenton" + 22*" " + "(pi)")
        print("Doble Queso" + 19*" " + "(dq)")
        print("Aceitunas" + 21*" " + "(ac)")
        print("Pepperoni" + 21*" " + "(pp)")
        print("Salchichón" + 20*" " + "(sa)")
        print()

        #Ciclo para el pedido de ingredientes
        while(_contI > 0):  
            _ingre= input("Indique ingrediente (enter para terminar): ")
            if(_ingre == '') and (_contI == 1):
                print("Usted seleccionó un sadwich " + str(_sand.get_tamano()) + " con Queso")
                _contI = 0
                
            elif(_ingre == "ja"):
                _ingreN = Ingrediente("Jamón")
                _listI.append(_ingreN.get_nombre())
                _contI += 1
                _total += _ingreN.get_precio()
                
            elif(_ingre == "ch"):
                _ingreN = Ingrediente("Champiñones")
                _listI.append(_ingreN.get_nombre())
                _contI += 1
                _total += _ingreN.get_precio()
                
            elif(_ingre == "pi"):
                _ingreN = Ingrediente("Pimentón")
                _listI.append(_ingreN.get_nombre())
                _contI += 1
                _total += _ingreN.get_precio()
                
            elif(_ingre == "dq"):
                _ingreN = Ingrediente("Doble Queso")
                _listI.append(_ingreN.get_nombre())
                _contI += 1
                _total += _ingreN.get_precio()
                
            elif(_ingre == "ac"):
                _ingreN = Ingrediente("Aceitunas")
                _listI.append(_ingreN.get_nombre())
                _contI += 1
                _total += _ingreN.get_precio()
                
            elif(_ingre == "pp"):
                _ingreN = Ingrediente("Pepperoni")
                _listI.append(_ingreN.get_nombre())
                _contI += 1
                _total += _ingreN.get_precio()
                
            elif(_ingre == "sa"):
                _ingreN = Ingrediente("Salchichón")
                _listI.append(_ingreN.get_nombre())
                _contI += 1
                _total += _ingreN.get_precio()
                
            else:
                print("Usted seleccionó un sandwiche " + str(_sand.get_tamano()) + " con " + str(ingredients(_listI)))
                _contI = 0
        
        #Aca se suma el precio del sandwiche, el total de precio de ingredientes y en caso de ser un segundo pedido en adelante se le suma lo que se llevaba       
        _totalF = _totalF + _sand.get_precio() + _total 
        # Se llama metodo de Modulo Factura para mostrar la misma
        _opcionM = f.factura(_sand.get_tamano(),_sand.get_precio(),_total,_contS,_totalF) 
        
        # En este if se reinician variables en caso de que se haga otro pedido
        if(_opcionM != 'n'):
            print("\n" * 100)
            del _sand
            del _ingreN
            _opcion = ''
            _opcionM = ''
            _contI = 1
            _contS += 1
            _listI = []
