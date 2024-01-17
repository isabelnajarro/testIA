from floresHerencia import Flor, Rosa, Amapola
import csv

class FlorManager:
    def __init__(self, csv_rosas):
        self.csv_rosas = "rosas.csv"
        self.csv_amapolas = "amapolas.csv"

    
def mostrar_info_rosas_csv(self):
        try:
            with open("rosas.csv", 'r') as archivo_csv:
                lector_csv = csv.DictReader(archivo_csv)
                for fila in lector_csv:
                    print(f"Nombre: {fila['Nombre']}, Tipo: {fila['Tipo']}, HorasSol: {fila['HorasSol']}, HorasMaxSol: {fila['HorasMaxSol']}, Color: {fila['Color']}")
        except FileNotFoundError:
            print("El archivo 'rosas.csv' no se encontró.")

def menu():
        while True:
            print("\nMenú:")
            print("1. Mostrar flores")
            print("2. Modificar horas de sol de una flor")
            print("3. Borrar flor")
            print("4. Buscar flores por tipo")
            print("5. Salir")

            opcion = input("Ingrese el número de la opción: ")

            if opcion == "1":
                mostrar_info_rosas_csv()#, nombre)
