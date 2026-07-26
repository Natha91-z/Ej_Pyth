# Escribir una funcion que calcule el total de una factura tras aplicarle el IVA.
#La funcion debe escribir la cantidad sin IVA y el porcentaje a aplicar, devolviendo el total de la factura.
#Si se invoca la funcion sin pasarle el %, debe aplicar un 21%.

def total():
    monto = float(input("Ingresa el valor del producto que estas pagando:"))
    iva = int(input("Ingresa el valor del IVA: "))
    
    if iva != 0:
        if iva > 0:
           totalPagar = ((monto * iva)/ 100) + monto
           return totalPagar
        else:
            return "El monto de IVA es negativo. No es posible"
    else:
        totalPagar = (monto* 0.21) + monto
        return totalPagar
    print("El total de su monto es: ", total())