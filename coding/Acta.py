from coding.DetActa import DetActa


class Acta:

    def __init__(self, profesor):
        self.profesor = profesor

    def imprimir(self):
        curso = self.profesor.curso
        for estudiante in curso.estudiantes:
            detActa = DetActa(estudiante)
            print(detActa.mostrarDatos())