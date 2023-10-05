class Notas:

    def __init__(self):
        self.notas = {
            'n1': 0,
            'n2': 0,
            'ex1': 0,
            'n3': 0,
            'n4': 0,
            'ex2': 0
        }

    def asignarNota(self):
        for nota in self.notas:
            self.notas[nota] = int(input(f"Ingrese la nota {nota}: "))
    
    def promedio1(self):
        return self.notas['n1'] + self.notas['n2'] + self.notas['ex1']

    def promedio2(self):
        return self.notas['n3'] + self.notas['n4'] + self.notas['ex2']

    def nota_final(self):
        return self.promedio1() + self.promedio2()

    def estado(self):
        return "Aprobado" if self.nota_final() >= 70 else "Reprobado"

    def mostrarDatos(self):
        return f"""
        Nota 1: {self.notas['n1']}
        Nota 2: {self.notas['n2']}
        Examen 1: {self.notas['ex1']}
        Nota 3: {self.notas['n3']}
        Nota 4: {self.notas['n4']}
        Examen 2: {self.notas['ex2']}
        Promedio 1: {self.promedio1()}
        Promedio 2: {self.promedio2()}
        Nota Final: {self.nota_final()}
        Estado: {self.estado()}
        """