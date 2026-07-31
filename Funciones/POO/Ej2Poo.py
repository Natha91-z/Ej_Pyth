# Realizar un programa el cual se declaren dos valores enteros utlizando
# el metodo __init__. Calcular la +, -,*. /. Usar el metodo de cada una y 
# llamar a la clase calculadora. Mostrar resultados. 




class calculadora():
    def __init__(self):
        self.num1 = int(input("Ingrese el primer valor: "))
        self.num2 = int(input("Ingrese el segundo valor: "))
        
    def suma(self):
        self.suma = self.num1 + self.num2
        return " El resultado es: ", self.suma
    
    def resta(self):
        self.resta = self.num1 - self.num2
        return " El resultado es: ", self.resta
    
    def multi(self):
            self.multi = self.num1 * self.num2
            return " El resultado es: ", self.multi
        
    def division(self): 
            self.division = self.num1 / self.num2
            return " El resultado es: ", self.division
        
calcular = calculadora()
print(calcular.suma())
print(calcular.resta())        
print(calcular.multi())
print(calcular.division())