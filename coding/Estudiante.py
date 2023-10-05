import IUsuario


class Estudiante(IUsuario):

    def __init__(self, nombre, apellido, notas):
        self.nombre = nombre
        self.apellido = apellido
        self.notas = notas

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def mostrarDatos(self):
        return "Nombre: " + self.nombre + " " + self.apellido