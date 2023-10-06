class DetActa:

    _secuencia = 0

    def __init__(self, id_acta, estudiante):
        DetActa._secuencia += 1
        self.id = DetActa._secuencia
        self.id_acta = id_acta
        self.estudiante = estudiante
    
    def mostrarDatos(self):
        return self.estudiante.mostrarDatos()
