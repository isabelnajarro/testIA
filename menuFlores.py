from floresHerencia import Flor, Rosa, Amapola
import csv

class FlorManager:
    def __init__(self):
        self.csv_rosas = "rosas.csv"
        self.rosas = []
        self.csv_amapolas = "amapolas.csv"
        self.amapolas = []
        self.leer_info_rosas()
        self.leer_info_amapolas()

    def leer_info_rosas(self):
        try:
            with open(self.csv_rosas, 'r') as archivo_csv:
                lector_csv = csv.DictReader(archivo_csv)
                for fila in lector_csv:
                    rosa = Rosa(fila['Nombre'], fila['Tipo'], int(fila['HorasSol']), int(fila['HorasMaxSol']), fila['Color'])
                    self.rosas.append(rosa)
        except FileNotFoundError:
            print(f"El archivo '{self.csv_rosas}' no se encontró.")

    def leer_info_amapolas(self):
            try:
                with open(self.csv_amapolas, 'r') as archivo_csv:
                    lector_csv = csv.DictReader(archivo_csv)
                    for fila in lector_csv:
                        amapola = Amapola(fila['Nombre'], fila['Tipo'], int(fila['HorasSol']), int(fila['HorasMaxSol']), fila['Temporada'])
                        self.amapolas.append(amapola)
            except FileNotFoundError:
                print(f"El archivo '{self.csv_rosas}' no se encontró.")
    
    def mostrar_rosas(self):
        for fila in self.rosas:
            print(f"Nombre: {fila['Nombre']}, Tipo: {fila['Tipo']}, HorasSol: {fila['HorasSol']}, HorasMaxSol: {fila['HorasMaxSol']}, Color: {fila['Color']}")
    
    def mostrar_amapolas(self):
        for fila in self.amapolas:
            print(f"Nombre: {fila['Nombre']}, Tipo: {fila['Tipo']}, HorasSol: {fila['HorasSol']}, HorasMaxSol: {fila['HorasMaxSol']}, Temporada: {fila['Temporada']}")


    def guardar_rosas(self, changes=False):
        try:
            with open(self.rosas, 'w', newline='') as archivo:
                campos = ["Nombre", "Tipo", "HorasSol", "HorasMaxSol", "Color"]
                escritor_csv = csv.DictWriter(archivo, fieldnames=campos)

                escritor_csv.writeheader()
                for flor in self.rosas:
                    escritor_csv.writerow({
                        "Nombre": flor.nombre,
                        "Tipo": flor.tipo,
                        "HorasSol": flor.horasSol,
                        "HorasMaxSol": flor.horasMaxSol,
                        "Color": flor.color 
                    })
            print(f"Se han guardado los datos en '{archivo_csv}'.")
        except Exception as e:
            print("Error")

    def guardar_amapolas(self):
        with open(self.csv_rosas, 'w', newline='') as archivo:
            campos = ["Nombre", "Tipo", "HorasSol", "HorasMaxSol", "Temporada"]
            escritor_csv = csv.DictWriter(archivo, fieldnames=campos)

            escritor_csv.writeheader()
            for flor in self.amapolas:
                escritor_csv.writerow({
                    "Nombre": flor.nombre,
                    "Tipo": flor.tipo,
                    "HorasSol": flor.horasSol,
                    "Temporada": flor.temporada,
                    "FechaRiego": flor.fechaRiego
                })

    def actualizarBD():
        print("Se procede a actualizar la base de datos de rosas")
        self.guardar_rosas()
        print("Se procede a actualizar la base de datos de amapolas")
        self.guardar_amapolas()

    def addRosa(self, nombre, tipo, horasSol, horasMaxSol, color):
        rosa = Rosa(fila['Nombre'], fila['Tipo'], int(fila['HorasSol']), int(fila['HorasMaxSol']), fila['Color'])
        self.rosas.append(rosa)
        self.guardar_rosas()

    def addAmapola(self, nombre, tipo, horasSol, horasMaxSol, temporada):
        amapola = Amapola(fila['Nombre'], fila['Tipo'], int(fila['HorasSol']), int(fila['HorasMaxSol']), fila['Temporada'])
        self.amapolas.append(amapola)
        self.guardar_rosas()


    def menu(self):
        while True:
            print("\nMenú:")
            print("1. Mostrar flores")
            print("2. Poner plantas al sol")
            print("3. Actualizar base de datos")
            print("4. Crear rosa")
            print("5. Crear amapola")

            opcion = input("Ingrese el número de la opción: ")

            if opcion == "1":
                opcion = input("Selecciona 1. Rosas o 2.Amapolas: ")
                if opcion == "1":
                    self.mostrar_rosas()
                else:
                    self.mostrar_amapolas()
            elif opcion == "2":
                opcion = input("Selecciona 1. Rosas o 2.Amapolas: ")
                horas = input("¿Cuántas horas quieres ponerlas al sol?")  
                if opcion == "1":
                    self.mostrar_rosas()
                elif opcion == "2":
                    self.mostrar_amapolas()
            elif opcion == "3":
                self.actualizarBD()
            #elif opcion == "4":
            #    campos = ["Nombre", "Tipo", "HorasSol", "HorasMaxSol", "Color"]
            #elif opcion == "5":


if __name__ == "__main__":
    manager = FlorManager()
    manager.menu()
