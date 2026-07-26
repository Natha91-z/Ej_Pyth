class A():
    def __init__(self):
        self._cuenta = 0
        self.__contador = 0
        
    @property       
    def cuenta(self):
        return self._cuenta
        
    @property
    def contador(self):
        return self.__contador
    
a = A()
print(a.cuenta)
print(a.contador)
    
        