import IUsuario
from coding.Acta import Acta


class Profesor(IUsuario):

    def __init__(self, nombre, apellido, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def mostrarDatos(self):
        return ("Nombre: " + self.nombre + " " + self.apellido)
