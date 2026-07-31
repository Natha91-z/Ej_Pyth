#Realizar un programa con una clase Estudiante, que tenga atributos nombre y nota.
#definir los metodos y mostrar resultados de la nota. 

class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        
    def imprimir(self):
        print("Nombre: {} \n Nota: {}". format(self.nombre, self.nota))
        
    def resultados(self):
        if self.nota < 7:
            print(" Perdiste")
        else:
            print(" Pasaste")    
        
estudiante1 = Estudiante ("Juan", 9)
estudiante1. imprimir()
estudiante1. resultados()

estudiante2 = Estudiante (" Pedro", 6)
estudiante2.imprimir()
estudiante2.resultados()