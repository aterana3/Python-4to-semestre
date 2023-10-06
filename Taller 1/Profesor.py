from IUsuario import IUsuario

class Profesor(IUsuario):

    def __init__(self, id, nombre, apellido):
        super().__init__(id, nombre, apellido)

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def mostrarDatos(self):
        return ("Nombre: " + self.nombre + " " + self.apellido)
