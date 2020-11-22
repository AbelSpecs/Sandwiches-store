class Ingrediente:
    #Propiedades de Ingrediente
    def __init__(self,nombre = ''):
        self.__nombre = nombre
        if(self.__nombre == "Jamón"):
            self.__precio = 40
            
        elif(self.__nombre == "Champiñones"):
            self.__precio = 35
            
        elif(self.__nombre == "Pimentón"):
            self.__precio = 30
            
        elif(self.__nombre == "Doble Queso"):
            self.__precio = 40
            
        elif(self.__nombre == "Aceitunas"):
            self.__precio = 57.5
            
        elif(self.__nombre == "Pepperoni"):
            self.__precio = 38.5
            
        elif(self.__nombre == "Salchichón"):
            self.__precio = 62.5
               
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        self.__nombre = nombre
        
    def get_precio(self):
        return self.__precio
    
    def set_precio(self,precio):
        self.__precio = precio  
        
    
    