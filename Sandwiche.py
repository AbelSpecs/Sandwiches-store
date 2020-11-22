class Sandwiche:
    #Propiedades de sandwiche
    def __init__(self,tamano =''):
        self.__tamano = tamano
        if(self.__tamano == 'Triple'):
            self.__precio = 580
        elif(self.__tamano == 'Doble'):
            self.__precio = 430
        elif(self.__tamano == 'Individual'):
            self.__precio = 280
        else:
            self.__precio = 0
        
    def get_tamano(self):
        return self.__tamano
    
    def set_tamano(self,tamano):
        self.__tamano = tamano
        
    def get_precio(self):
        return self.__precio
    
    def set_precio(self,precio):
        self.__precio = precio    