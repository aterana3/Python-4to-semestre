from datetime import date, datetime

list_dets = []


class Facultad:

    _secuencia = 0

    def __init__(self, nombre):
        Facultad._secuencia += 1
        self.id = Facultad._secuencia
        self.nombre = nombre

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

class Semestre:

    _secuencia = 0

    def __init__(self, nombre, fecha_inicio, fecha_final):
        Semestre._secuencia += 1
        self.id = Semestre._secuencia
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getFechaInicio(self):
        return self.fecha_inicio
    
    def getFechaFinal(self):
        return self.fecha_final

class Carrera:

    _secuencia = 0

    def __init__(self, nombre):
        Carrera._secuencia += 1
        self.id = Carrera._secuencia
        self.nombre = nombre

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

class Paralelo:

    _secuencia = 0

    def __init__(self, nombre, seccion):
        Paralelo._secuencia += 1
        self.id = Paralelo._secuencia
        self.nombre = nombre
        self.seccion = seccion

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getSeccion(self):
        return self.seccion

class Asignatura:

    _secuencia = 0

    def __init__(self, nombre):
        Asignatura._secuencia += 1
        self.id = Asignatura._secuencia
        self.nombre = nombre

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre


class Profesor:

    _secuencia = 0

    def __init__(self, nombre, apellido):
        Profesor._secuencia += 1
        self.id = Profesor._secuencia
        self.nombre = nombre
        self.apellido = apellido

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

class Estudiante:

    _secuencia = 0

    def __init__(self, nombre, apellido):
        Estudiante._secuencia += 1
        self.id = Estudiante._secuencia
        self.nombre = nombre
        self.apellido = apellido

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

class Notas:

    _secuencia = 0

    def __init__(self, nombre_estudiante, n1, n2, ex1, n3, n4, ex2):
        Notas._secuencia += 1
        self.id = Notas._secuencia
        self.nombre_estudiante = nombre_estudiante
        self.n1 = n1
        self.n2 = n2
        self.ex1 = ex1
        self.n3 = n3
        self.n4 =  n4
        self.ex2 = ex2

    def getId(self):
        return self.id

    def getNombreEstud(self):
        return self.nombre_estudiante

    def getN1(self):
        return self.n1

    def getN2(self):
        return self.n2

    def getEx1(self):
        return self.ex1

    def getN3(self):
        return self.n3

    def getN4(self):
        return self.n4

    def getEx2(self):
        return self.ex2

    def promedio1(self):
        return self.n1 + self.n2 + self.ex1

    def promedio2(self):
        return self.n3 + self.n4 + self.ex2

    def nota_final(self):
        return self.promedio1() + self.promedio2()

    def estado(self):
        return "Aprobado" if self.nota_final() >= 70 else "Reprobado"

    def mostrarDatos(self):
        return f"{self.nombre_estudiante} | N1: {self.n1} | N2: {self.n2} | EX1: {self.ex1}| N3: {self.n3} | N4: {self.n4} | EX2: {self.ex2} | NF: {self.nota_final()}| Estado {self.estado()}"

class Acta:

    _secuencia = 0  

    def __init__(self, nombre_facu, nombre_semes, nombre_carre, nombre_prof, nombre_sec, nombre_asign, nombre_para, fecha_inicio, fecha_final, fecha_acta):
        Acta._secuencia += 1
        self.id = Acta._secuencia
        self.nombre_facu = nombre_facu
        self.nombre_semes = nombre_semes
        self.nombre_carre = nombre_carre
        self.nombre_prof = nombre_prof
        self.nombre_sec = nombre_sec
        self.nombre_asign = nombre_asign
        self.nombre_para = nombre_para
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self.fecha_acta = fecha_acta

    def getId(self):
        return self.id

    def getPeriodo(self):
        mes_inicio = fecha_inicio.strftime('%B')
        mes_final = fecha_final.strftime('%B')
        año = fecha_inicio.year
        return f"{mes_inicio} - {mes_final}  {año}"

    def imprimir(self):
        print("UNEMI")
        print(f"Acta de calificaciones - {self.fecha_acta}")
        print(f"Periodo: {self.getPeriodo()}")
        print("----------------------------------------")
        print(f"Facultad: {self.nombre_facu}")
        print(f"Carrera: {self.nombre_carre}")
        print(f"Semestre: {self.nombre_semes}                       Paralelo: {self.nombre_para}")
        print(f"Profesor: {self.nombre_prof}                        Asignatura: {self.nombre_asign}")
        print(f"Seccion: {self.nombre_sec}                   Inicio: {self.fecha_inicio} - Fin: {self.fecha_final}")
        print("----------------------------------------")
        print("Estudiante | N1 | N2 | EX1 | N3 | N4 | EX2 | NF | Estado")
        for det in list_dets:
            print(det.getNotas().mostrarDatos())
        print("----------------------------------------")


class DetActa:

    _secuencia = 0

    def __init__(self, id_Acta, Notas):
        DetActa._secuencia += 1
        self.id = DetActa._secuencia
        self.id_Acta = id_Acta
        self.Notas = Notas

    def getId(self):
        return self.id

    def getId_Acta(self):
        return self.id_Acta

    def getNotas(self):
        return self.Notas


facultad = Facultad("FACI")
carrera = Carrera("Software")
fecha_inicio = date(2023, 4, 24)
fecha_final = date(2023, 8, 20) 
semestre = Semestre("1er Nivel", fecha_inicio, fecha_final)
paralelo = Paralelo("A1", "Nocturno")
asignatura = Asignatura("Algoritmo y logica de programacion")
profesor = Profesor("Daniel", "Vera")
estudiante_1 = Estudiante("Juan", "Perez")
estudiante_2 = Estudiante("Maria", "Gomez")
nota_1 = Notas(estudiante_1.getNombre(), 10, 10, 10, 10, 10, 10)
nota_2 = Notas(estudiante_2.getNombre(), 10, 10, 10, 10, 10, 10)
fecha_actual = datetime.now().date()
acta = Acta(facultad.getNombre(), semestre.getNombre(), carrera.getNombre(), profesor.getNombre(), paralelo.getSeccion(), asignatura.getNombre(), paralelo.getNombre(), semestre.getFechaInicio(), semestre.getFechaFinal(), fecha_actual)
detActa_1 = DetActa(acta.getId(), nota_1)
detActa_2 = DetActa(acta.getId(), nota_2)
list_dets.append(detActa_1)
list_dets.append(detActa_2)
acta.imprimir()