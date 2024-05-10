import csv
import os

class Estudiante:
    def __init__(self,Carnet, Nombres, Apellidos, ListadoNotas):
        self.Carnet=Carnet
        self.Nombres=Nombres
        self.Apellidos=Apellidos
        self.ListadoNotas=ListadoNotas
    
    def mostrarPromedio(self):
        total_notas = 0

        for nota in self.ListadoNotas:
            total_notas += nota.nota
        promedio = total_notas / len(self.ListadoNotas)
        return promedio
    
    def obtenerCursoConNotaMasAlta(self):

        lista_notas = []
        for nota in self.ListadoNotas:
            lista_notas.append(nota.nota)
        return max(lista_notas)
    
    def obtenerCursoConNotaMasBaja(self):
        lista_notas = []
        for nota in self.ListadoNotas:
            lista_notas.append(nota.nota)
        return min(lista_notas)

class Notas:
    def __init__ (self, curso, nota):
        self.curso=curso
        self.nota=nota


base_dir = r"E:\Projects\Python"
file_name = 'Notas.csv'
file_path = os.path.join(base_dir, file_name)

def leer_archivo(nombre_archivo):
    estudiantes = []

    with open(nombre_archivo, newline='') as archivo_csv:
        lector_csv  = csv.reader(archivo_csv, delimiter=';')
        next(lector_csv)
        for row in lector_csv:
            carnet = int(row[0])
            nombres = (row[1])
            apellidos = (row[2])
            notas = [Notas(row[i], int(row[i+1])) for i in range (3, len(row), 2)]
            estudiante = Estudiante(carnet, nombres, apellidos, notas)
            estudiantes.append(estudiante)
                
    return estudiantes


estudiantes = leer_archivo(file_path)

for estudiante in estudiantes:
    print("Carnet: ", estudiante.Carnet)
    print("Nombres: ", estudiante.Nombres)
    print("Apellidos :", estudiante.Apellidos)
    print("Notas :")
    for nota in estudiante.ListadoNotas:
        print( "    Curso: ",nota.curso, ":" , nota.nota)
    print("Promedio",estudiante.mostrarPromedio())
    print("Nota mas alta", estudiante.obtenerCursoConNotaMasAlta())
    print("Nota mas baja", estudiante.obtenerCursoConNotaMasBaja())

def estudiantePromedioMasAlto(estudiantes):

    estudiantePromedioMasAlto = estudiantes[0]
    promedioMaximo = estudiantePromedioMasAlto.mostrarPromedio()

    for estudiante in estudiantes[1:]:
        promedioActual = estudiante.mostrarPromedio()

        if promedioActual > promedioMaximo:
            estudiantePromedioMasAlto = estudiante
            promedioMaximo = promedioActual

    return print("Estudiante con Promedio mas alto: ", estudiantePromedioMasAlto.Nombres, ", Promedio: ", promedioMaximo)

estudiantePromedioMasAlto(estudiantes)
