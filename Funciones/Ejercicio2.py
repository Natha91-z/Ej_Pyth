# Escribir una funcion que reciba un numero entero positivo y devuelva su factorial

from math import factorial as math_factorial

def factorial():
    num = int(input("Ingresa tu numero entero positivo: "))
    if num > 0:
        print(math_factorial(num))
    else:
        print("El numero es negativo, no continuar")
        
factorial()