# Crear una clase llamada Marino(), con un metodo que sea hablar, en donde muestre un mensaje que diga "Hola...". Luego, crear una clase Pulpo() que herede Marino, pero modificar el mensaje de hablar por "Soy un Pulpo". Por ultimo, crear una clase Foca(), heredada de Marino, pero que tenga un atributo nuevo llamado mensaje y que muestre ese mesjae como parametro

class Universidad():
    def __init__(self,Nombre):
        self.Nombre = Nombre
        
class Carrera():
    def carrera(self,especialidad):
        self.especialidad = especialidad
        
class Estudiante(Universidad,Carrera):
    def datos(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        print("Mi nombre es {}, tengo {}, años, mi especialidad es {}.\nEstudio en la universidad {}".format(self.nombre,self.edad,self.especialidad,self.nombre))
        
persona = Estudiante("Don Bosco")
persona.carrera("Sistemas")
persona.datos("Nath")
