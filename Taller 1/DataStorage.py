import json
from pathlib import Path

Fl_Ruta_Configuration = Path("C:/SistemaActa/configuracion.txt")
Fl_Ruta_File = Path("C:/SistemaActa/estudiantes.json")

def init():
    if not Fl_Ruta_File.parent.exists():
        Fl_Ruta_File.parent.mkdir()
        print("Se creó la carpeta", Fl_Ruta_File.parent)

    if not Fl_Ruta_File.exists():
        with open(Fl_Ruta_File, 'w') as archivo_estudiantes:
            archivo_estudiantes.write("{}")
            print("Se creó el archivo para los contactos", Fl_Ruta_File)

    if not Fl_Ruta_Configuration.exists():
        with open(Fl_Ruta_Configuration, 'w') as archivo_configuracion:
             archivo_configuracion.write("Estudiantes:0")
             archivo_configuracion.write("\n")
             archivo_configuracion.write("Profesor: ")
        print("Se creó el archivo para la configuracion", Fl_Ruta_Configuration)


def recuperarRegistro():
    with open(Fl_Ruta_File, 'r') as archivo_estudiantes:
        estudiantes = json.load(archivo_estudiantes)
    return estudiantes

def guardarRegistro(estudiantes):
    with open(Fl_Ruta_File, 'w') as archivo_estudiantes:
        json.dump(estudiantes, archivo_estudiantes, indent=4)

