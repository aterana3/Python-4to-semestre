class Curso:

    def __init__(self, nombre, estudiantes):
        self.nombre = nombre
        self.estudiantes = estudiantes

    def getNombre(self):
        return self.nombre

    def getEstudiantes(self):
        return self.estudiantes