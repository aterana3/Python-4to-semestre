from datetime import date, datetime
import json
from pathlib import Path

Fl_Ruta_Raiz = Path("C:/Acta/")

lista_archivos = {
    'facultad': Path('C:/Acta/facultad.json'),
    'semestre': Path('C:/Acta/semestre.json'),
    'carrera': Path('C:/Acta/carrera.json'),
    'paralelo': Path('C:/Acta/paralelo.json'),
    'asignatura': Path('C:/Acta/asignatura.json'),
    'profesor': Path('C:/Acta/profesor.json'),
    'estudiante': Path('C:/Acta/estudiante.json'),
    'notas': Path('C:/Acta/notas.json'),
    'acta': Path('C:/Acta/acta.json'),
    'detActa': Path('C:/Acta/detActa.json')
}


class Facultad:

    _secuencia = len(json.load(open(lista_archivos['facultad'], 'r'))) if lista_archivos['facultad'].exists() else 0

    def __init__(self, nombre):
        Facultad._secuencia += 1
        self.id = Facultad._secuencia
        self.nombre = nombre

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

class Semestre:

    _secuencia = len(json.load(open(lista_archivos['semestre'], 'r'))) if lista_archivos['semestre'].exists() else 0

    def __init__(self, nombre):
        Semestre._secuencia += 1
        self.id = Semestre._secuencia
        self.nombre = nombre

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

    _secuencia = len(json.load(open(lista_archivos['paralelo'], 'r'))) if lista_archivos['paralelo'].exists() else 0

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

    _secuencia = len(json.load(open(lista_archivos['asignatura'], 'r'))) if lista_archivos['asignatura'].exists() else 0

    def __init__(self, nombre, nombre_facu, nombre_semes, nombre_carre, nombre_secc, nombre_para, nombre_prof, estudiantes):
        Asignatura._secuencia += 1
        self.id = Asignatura._secuencia
        self.nombre = nombre
        self.nombre_facu = nombre_facu
        self.nombre_semes = nombre_semes
        self.nombre_carre = nombre_carre
        self.nombre_secc = nombre_secc
        self.nombre_para = nombre_para
        self.nombre_prof = nombre_prof
        self.estudiantes = estudiantes
        
    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre
    
    def getNombreFacultad(self):
        return self.nombre_facu
    
    def getNombreSemestre(self):
        return self.nombre_semes
    
    def getNombreCarrera(self):
        return self.nombre_carre
    
    def getNombreSeccion(self):
        return self.nombre_secc
    
    def getNombreParalelo(self):
        return self.nombre_para
    
    def getNombreProfesor(self):
        return self.nombre_prof
    
    def getEstudiantes(self):
        return self.estudiantes
    
    def generarActa(self):
        print("UNEMI")
        print(f"Acta de calificaciones - ")
        print("----------------------------------------")
        print(f"Facultad: {self.nombre_facu}")
        print(f"Carrera: {self.nombre_carre}")
        print(f"Semestre: {self.nombre_semes}                       Paralelo: {self.nombre_para}")
        print(f"Profesor: {self.nombre_prof}                        Asignatura: {self.nombre}")
        print(f"Seccion: {self.nombre_secc}")
        print("----------------------------------------")
        print("Estudiante | N1 | N2 | EX1 | N3 | N4 | EX2 | NF | Estado")
        with open(lista_archivos['estudiante']) as archivoEstudiante:
            datos_estudiantes = json.load(archivoEstudiante)
            if len(datos_estudiantes) == 0:
                print("No hay estudiantes registrados")
                return
            for id_estudiante, estudiante in datos_estudiantes.items():
                if int(id_estudiante) in [datos_estudiante for datos_estudiante in self.estudiantes]:
                
                    print(f"{estudiante['nombre']} {estudiante['apellido']} | ", end="")
                    
                    with open(lista_archivos['notas']) as archivoNotas:
                        datos_notas = json.load(archivoNotas)
                        if len(datos_notas) == 0:
                            print("No hay notas registrados")
                            return
                        for id_nota, nota in datos_notas.items():
                            print(f"{nota['n1']} | {nota['n2']} | {nota['ex1']} | {nota['n3']} | {nota['n4']} | {nota['ex2']} | {nota['nota_final']} | {nota['estado']}")
                        
                    
                       
class Profesor:

    _secuencia = len(json.load(open(lista_archivos['profesor'], 'r'))) if lista_archivos['profesor'].exists() else 0

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

    _secuencia = len(json.load(open(lista_archivos['estudiante'], 'r'))) if lista_archivos['estudiante'].exists() else 0

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

    _secuencia = len(json.load(open(lista_archivos['notas'], 'r'))) if lista_archivos['notas'].exists() else 0

    def __init__(self, id_asignatura, id_estudiante, n1, n2, ex1, n3, n4, ex2):
        Notas._secuencia += 1
        self.id = Notas._secuencia
        self.id_asignatura = id_asignatura
        self.id_estudiante = id_estudiante
        self.n1 = n1
        self.n2 = n2
        self.ex1 = ex1
        self.n3 = n3
        self.n4 =  n4
        self.ex2 = ex2

    def getId(self):
        return self.id

    def getIdAsignatura(self):
        return self.id_asignatura

    def getIdEstudiante(self):
        return self.id_estudiante

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
        return f"N1: {self.n1} | N2: {self.n2} | EX1: {self.ex1}| N3: {self.n3} | N4: {self.n4} | EX2: {self.ex2} | NF: {self.nota_final()}| Estado {self.estado()}"


def inicializarArchivos():
    try:
        Lb_Existe_Ruta = Fl_Ruta_Raiz.exists()
        if not Lb_Existe_Ruta:
            Fl_Ruta_Raiz.mkdir()
            print(f"Se ha creado la carpeta del sistema {Fl_Ruta_Raiz}")
            for lista, ruta_archivo in lista_archivos.items():
                if not ruta_archivo.exists():
                    with open(ruta_archivo, 'w') as archivosDatos:
                        archivosDatos.write("{}")
                        print("Se creó el archivo para los datos del sistema", lista)
    except IOError:
        print("Hubo un error al crear la carpeta")
    

def menu():
    while True:
        print("Seleccione que desea hacer:")
        print("1.- Crear Facultad")
        print("2.- Crear Semestre")
        print("3.- Crear Carrera")
        print("4.- Crear Paralelo")
        print("5.- Crear Profesor")
        print("6.- Crear Estudiante")
        print("7.- Crear Asignatura")
        print("8.- Crear Notas")
        print("9.- Generar Acta")
        print("10.- Salir")
        try:
            opcion = int(input("Ingrese la opción: "))
            if opcion == 1:
                crearFacultad()
            if opcion == 2:
                crearSemestre()
            if opcion == 3:
                crearCarrera()
            if opcion == 4:
                crearParalelo()
            if opcion == 5:
                crearProfesor()
            if opcion == 6:
                crearEstudiante()
            if opcion == 7:
                crearAsignatura()
            if opcion == 8:
                crearNotas()
            if opcion == 9:
                generarActa()
                break
            if opcion == 10:
                print("Gracias por usar el sistema")
                break
        except ValueError:
            print("Ha introducido una opcion no valida")
    

def crearFacultad():
    nombre = input("Ingrese el nombre de la facultad: ")
    facultad = Facultad(nombre)
    with open(lista_archivos['facultad'], 'r') as archivoFacultad:
        datos = json.load(archivoFacultad)
        datos[facultad.getId()] = {
            'id': facultad.getId(),
            'nombre': facultad.getNombre()
        }
    with open(lista_archivos['facultad'], 'w') as archivoFacultad:
        json.dump(datos, archivoFacultad, indent=4)
    print("Se ha creado la facultad correctamente")


def crearSemestre():
    nombre = input("Ingrese el nombre del semestre: ")
    semestre = Semestre(nombre)
    with open(lista_archivos['semestre'], 'r') as archivoSemestre:
        datos = json.load(archivoSemestre)
        datos[semestre.getId()] = {
            'id': semestre.getId(),
            'nombre': semestre.getNombre(),
        }
    with open(lista_archivos['semestre'], 'w') as archivoSemestre:
        json.dump(datos, archivoSemestre, indent=4)
    print("Se ha creado el semestre correctamente")


def crearCarrera():
    nombre = input("Ingrese el nombre de la carrera: ")
    carrera = Carrera(nombre)
    with open(lista_archivos['carrera'], 'r') as archivoCarrera:
        datos = json.load(archivoCarrera)
        datos[carrera.getId()] = {
            'id': carrera.getId(),
            'nombre': carrera.getNombre()
        }
    with open(lista_archivos['carrera'], 'w') as archivoCarrera:
        json.dump(datos, archivoCarrera, indent=4)
    print("Se ha creado la carrera correctamente")


def crearParalelo():
    nombre = input("Ingrese el nombre del paralelo: ")
    seccion = input("Ingrese la seccion del paralelo: ")
    paralelo = Paralelo(nombre, seccion)
    with open(lista_archivos['paralelo'], 'r') as archivoParalelo:
        datos = json.load(archivoParalelo)
        datos[paralelo.getId()] = {
            'id': paralelo.getId(),
            'nombre': paralelo.getNombre(),
            'seccion': paralelo.getSeccion()
        }
    with open(lista_archivos['paralelo'], 'w') as archivoParalelo:
        json.dump(datos, archivoParalelo, indent=4)
    print("Se ha creado el paralelo correctamente")


def crearAsignatura():
    nombre = input("Ingrese el nombre de la asignatura: ")
    nombre_facultad = ""
    with open(lista_archivos['facultad'], 'r') as archivoFacultad:
        datos = json.load(archivoFacultad)
        if len(datos) == 0:
            print("No hay facultad registradas")
            return
        print("Seleccione la facultad")
        for id, facultad in datos.items():
            print(f"{id}.- {facultad['nombre']}")
            while True:
                try:
                    valor = input("Ingrese Id de la Facultad: ")
                    if int(valor) in [datos_archivo['id'] for datos_archivo in datos.values()]:
                        facultad = datos[valor]
                        nombre_facultad = facultad['nombre']
                        break
                except ValueError:
                    print("ID de estado no válido. Intente nuevamente.")    
    nombre_semestre = ""
    with open(lista_archivos['semestre'], 'r') as archivoSemestre:
        datos = json.load(archivoSemestre)
        if len(datos) == 0:
            print("No hay semestre registrados")
            return
        print("Seleccione el semestre")
        for id, semestre in datos.items():
            print(f"{id}.- {semestre['nombre']}")
            while True:
                try:
                    valor = input("Ingrese Id del semestre: ")
                    if int(valor) in [datos_archivo['id'] for datos_archivo in datos.values()]:
                        semestre = datos[valor]
                        nombre_semestre = semestre['nombre']
                        break
                except ValueError:
                    print("ID de estado no válido. Intente nuevamente.")

    nombre_carrera = ""
    with open(lista_archivos['carrera'], 'r') as archivoCarrera:
        datos = json.load(archivoCarrera)
        if len(datos) == 0:
            print("No hay carrera registrados")
            return
        print("Seleccione la carrera")
        for id, carrera in datos.items():
            print(f"{id}.- {carrera['nombre']}")
            while True:
                try:
                    valor = input("Ingrese Id de la carrera: ")
                    if int(valor) in [datos_archivo['id'] for datos_archivo in datos.values()]:
                        carrera = datos[valor]
                        nombre_carrera = carrera['nombre']
                        break
                except ValueError:
                    print("ID de estado no válido. Intente nuevamente.")
                    
    nombre_paralelo = ""
    nombre_seccion = ""
    with open(lista_archivos['paralelo'], 'r') as archivoParalelo:
        datos = json.load(archivoParalelo)
        if len(datos) == 0:
            print("No hay paralelo registrados")
            return
        print("Seleccione el paralelo")
        for id, paralelo in datos.items():
            print(f"{id}.- {paralelo['nombre']} {paralelo['seccion']}")
            while True:
                try:
                    valor = input("Ingrese Id del paralelo: ")
                    if int(valor) in [datos_archivo['id'] for datos_archivo in datos.values()]:
                        paralelo = datos[valor]
                        nombre_paralelo = paralelo['nombre']
                        nombre_seccion = paralelo['seccion']
                        break
                except ValueError:
                    print("ID de estado no válido. Intente nuevamente.")
    
    nombre_profesor = ""
    with open(lista_archivos['profesor'], 'r') as archivoProfesor:
        datos = json.load(archivoProfesor)
        if len(datos) == 0:
            print("No hay profesor registrados")
            return
        print("Seleccione el profesor")
        for id, profesor in datos.items():
            print(f"{id}.- {profesor['nombre']} {profesor['apellido']}")
            while True:
                try:
                    valor = input("Ingrese Id del profesor: ")
                    if int(valor) in [datos_archivo['id'] for datos_archivo in datos.values()]:
                        profesor = datos[valor]
                        nombre_profesor = profesor['nombre'] + " " + profesor['apellido']
                        break
                except ValueError:
                    print("ID de estado no válido. Intente nuevamente.")     
                           
    estudiantes = []
    with open(lista_archivos['estudiante'], 'r') as archivoEstudiante:
        datos = json.load(archivoEstudiante)
        if len(datos) == 0:
            print("No hay estudiantes registrados")
            return
        print("Seleccione los estudiantes")
        for id, estudiante in datos.items():
            print(f"{id}.- {estudiante['nombre']} {estudiante['apellido']}")
            while True:
                try:
                    valor = input("Ingrese Id del estudiante (Terminar = salir): ")
                    if valor == "Terminar":
                        break
                    elif int(valor) in [datos_archivo['id'] for datos_archivo in datos.values()]:
                        estudiante = datos[valor]
                        id_estudiante = estudiante['id']
                        if estudiante['id'] in estudiantes:
                            print("El estudiante ya ha sido seleccionado")
                        else:
                            estudiantes.append(id_estudiante)
                except ValueError:
                    print("ID de estado no válido. Intente nuevamente.")
    asignatura = Asignatura(nombre, nombre_facultad, nombre_semestre, nombre_carrera, nombre_seccion, nombre_paralelo, nombre_profesor, estudiantes)
    with open(lista_archivos['asignatura'], 'r') as archivoAsignatura:
        datos = json.load(archivoAsignatura)
        datos[asignatura.getId()] = {
            'id': asignatura.getId(),
            'nombre': asignatura.getNombre(),
            'nombre_facultad': asignatura.nombre_facu,
            'nombre_semestre': asignatura.nombre_semes,
            'nombre_carrera': asignatura.nombre_carre,
            'nombre_seccion': asignatura.nombre_secc,
            'nombre_paralelo': asignatura.nombre_para,
            'nombre_profesor': asignatura.nombre_prof,
            'estudiantes': asignatura.estudiantes
        }
    with open(lista_archivos['asignatura'], 'w') as archivoAsignatura:
        json.dump(datos, archivoAsignatura, indent=4)
    
    
def crearProfesor():
    nombre = input("Ingrese el nombre del profesor: ")
    apellido = input("Ingrese el apellido del profesor: ")
    profesor = Profesor(nombre, apellido)
    with open(lista_archivos['profesor'], 'r') as archivoProfesor:
        datos = json.load(archivoProfesor)
        datos[profesor.getId()] = {
            'id': profesor.getId(),
            'nombre': profesor.getNombre(),
            'apellido': profesor.getApellido()
        }
    with open(lista_archivos['profesor'], 'w') as archivoProfesor:
        json.dump(datos, archivoProfesor, indent=4)
    print("Se ha creado el profesor correctamente")
    

def crearEstudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    estudiante = Estudiante(nombre, apellido)
    with open(lista_archivos['estudiante'], 'r') as archivoEstudiante:
        datos = json.load(archivoEstudiante)
        datos[estudiante.getId()] = {
            'id': estudiante.getId(),
            'nombre': estudiante.getNombre(),
            'apellido': estudiante.getApellido()
        }
    with open(lista_archivos['estudiante'], 'w') as archivoEstudiante:
        json.dump(datos, archivoEstudiante, indent=4)
    print("Se ha creado el estudiante correctamente")
    
    
def crearNotas():
    asignatura = {}
    with open(lista_archivos['asignatura'], 'r') as archivoAsignatura:
        datos = json.load(archivoAsignatura)
        if len(datos) == 0:
            print("No hay asignaturas registradas")
            return
        print("Seleccione la asignatura")
        for id, asignatura in datos.items():
            print(f"{id}.- {asignatura['nombre']}")
            while True:
                try:
                    valor = input("Ingrese Id de la asignatura: ")
                    if int(valor) in [datos_archivo['id'] for datos_archivo in datos.values()]:
                        asignatura = datos[valor]
                        break
                except ValueError:
                    print("ID de estado no válido. Intente nuevamente.")
                    
    with open(lista_archivos['estudiante']) as archivoEstudiante:
        datos_estudiantes = json.load(archivoEstudiante)
        if len(datos_estudiantes) == 0:
            print("No hay estudiantes registrados")
            return
        print("Seleccione el estudiante")
        for id, estudiante in datos_estudiantes.items():
             if int(id) in [datos_estudiante for datos_estudiante in asignatura['estudiantes']]:
                print(f"{id}.- {estudiante['nombre']} {estudiante['apellido']}")
                while True:
                    try:
                        valor = input("Ingrese Id del estudiante: ")
                        if int(valor) in [datos_archivo['id'] for datos_archivo in datos_estudiantes.values()]:
                            datos = datos_estudiantes[valor]
                            n1 = int(input("Ingrese la nota 1: "))
                            n2 = int(input("Ingrese la nota 2: "))
                            ex1 = int(input("Ingrese el examen 1: "))
                            n3 = int(input("Ingrese la nota 3: "))
                            n4 = int(input("Ingrese la nota 4: "))
                            ex2 = int(input("Ingrese el examen 2: "))
                            notas = Notas(asignatura['id'], int(valor), n1, n2, ex1, n3, n4, ex2)
                            datos[notas.getId()] = {
                                'id': notas.getId(),
                                'id_asignatura': notas.getIdAsignatura(),
                                'id_estudiante': notas.getIdEstudiante(),
                                'n1': notas.getN1(),
                                'n2': notas.getN2(),
                                'ex1': notas.getEx1(),
                                'n3': notas.getN3(),
                                'n4': notas.getN4(),
                                'ex2': notas.getEx2(),
                                'nota_final': notas.nota_final(),
                                'estado': notas.estado()
                            }
                            with open(lista_archivos['notas'], 'w') as archivoNotas:
                                json.dump(datos, archivoNotas, indent=4)
                                print(f"Se ha creado las notas de {estudiante['nombre']} correctamente en la asignatura {asignatura['nombre']}")
                            break
                    except ValueError:
                        print("ID de estado no válido. Intente nuevamente.")
    
def generarActa():
    with open(lista_archivos['asignatura'], 'r') as archivoAsignatura:
        datos = json.load(archivoAsignatura)
        if len(datos) == 0:
            print("No hay asignaturas registradas")
            return
        print("Seleccione la asignatura")
        for id, asignatura in datos.items():
            print(f"{id}.- {asignatura['nombre']}")
            while True:
                try:
                    valor = input("Ingrese Id de la asignatura: ")
                    if int(valor) in [datos_archivo['id'] for datos_archivo in datos.values()]:
                        datos_asignatura = datos[valor]
                        asignatura = Asignatura(datos_asignatura['nombre'], datos_asignatura['nombre_facultad'], datos_asignatura['nombre_semestre'], datos_asignatura['nombre_carrera'], datos_asignatura['nombre_seccion'], datos_asignatura['nombre_paralelo'], datos_asignatura['nombre_profesor'], datos_asignatura['estudiantes'])
                        asignatura.generarActa()
                        break
                except ValueError:
                    print("ID de estado no válido. Intente nuevamente.")
    

if __name__ == "__main__":
    inicializarArchivos()
    menu()