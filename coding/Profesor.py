import IUsuario
from coding.Acta import Acta


class Profesor(IUsuario):

    def __init__(self, nombre, apellido, cedula, curso):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.curso = curso

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def mostrarDatos(self):
        print("Nombre: " + self.nombre + " " + self.apellido)

    def generarActa(self):
        acta = Acta(self)
        acta.imprimir()

    #Hola este es un documento de prueba