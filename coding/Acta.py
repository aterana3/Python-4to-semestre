from coding.DetActa import DetActa


class Acta:

    def __init__(self, curso):
        self.curso = curso

    def imprimir(self):
        for estudiante in self.curso.getEstudiantes():
            detActa = DetActa(estudiante)
            print(detActa.mostrarDatos())