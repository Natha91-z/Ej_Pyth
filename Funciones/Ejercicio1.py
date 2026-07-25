## Crear un programa que tenga una lista, luego crear una funcion con la cual
## se van a pedir al usuario numeros para agresar a la lista. 
## Se debe crear una funcion en donde se ordenen los numeros pares e impares dentro de las listas.

lista = []
num = 0 

def pedir():
    i = 0 
    while i <= 5:
        num = float(input("Ingresa un numero: "))
        lista.append(num)
        i += 1
       
pedir()
print(lista)

def ordenar():
    lista.sort()
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    print(pares)
    print(impares)
    
    pedir()
    ordenar()