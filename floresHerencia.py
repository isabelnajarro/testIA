from abc import ABC, abstractmethod
from datetime import datetime

FLORESDISPONIBLES = ["Amapola", "Margarita"]

class Flor(ABC):
    def __init__(self, nombre, tipo, horasSol, horasMaxSol):
        self.nombre = nombre
        self.tipo = tipo
        self.horasSol = horasSol
        self.horasMaxSol = horasMaxSol
        self.fechaRiego = datetime.now()

    @abstractmethod
    def darComida(self):
        pass

    def cambiarTierra(self):
        pass

    @staticmethod
    def isAvailable(tipo):
        return tipo in FLORESDISPONIBLES
    
    def __iter__(self):
        self.horasSol = self.horasMaxSol - self.horasSol
        return self
    
    def horasAlSolDisponibles():
        return 
    
    def sumarHorasSol(self, horas):
        self.horasSol += horas
        if self.horasSol >= self.horasMaxSol:
            print("La planta necesita agua, se procede a regar")
            self.fechaRiego = datetime.now()
            self.horasSol = 0
            print(f'Actualizada fecha riego a {self.fechaRiego} y las horas al sol a {self.horasSol}')

class Rosa(Flor):
    def __init__(self, nombre, tipo, horasSol, horasMaxSol, color):
        super().__init__(nombre, tipo, horasSol, horasMaxSol)
        self.color = color

    def darComida(self):
        print(f"Rosa de color {self.color} ha comido")
    
    def cambiarTierra(self):
        return self.horasSol > 2

class Amapola(Flor):
    def __init__(self, nombre, tipo, horasSol, horasMaxSol, temporada):
        super().__init__(nombre, tipo, horasSol, horasMaxSol)
        self.temporada = temporada

    def darComida(self):
        print(f"Amapola de temporada {self.temporada} ha comido")
    
    def cambiarTierra(self):
        return self.horasSol > 2
    
    '''
    def is_en_temporada(self):
        fecha_actual = datetime.now()
        return fecha_actual < datetime.strptime(self.temporada, "%Y-%m-%d")
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.is_en_temporada():
            return f"Amapola {self.nombre} está en temporada."
        else:
            raise StopIteration(f"Amapola {self.nombre} no está en temporada.")
    '''



# Crear instancias de las subclases
#rosa_azul = Rosa("Rosa", "Canina", 5, "Azul")
#amapola_roja = Amapola("Amapola", "Oriental", 3, "Verano")

# Llamar a los métodos de las subclases
#print("Resultado a si se le puede cambiar la tierra (Rosa): ", rosa_azul.cambiarTierra())
#print("¿Está disponible? (Rosa): ", rosa_azul.isAvailable(rosa_azul.tipo))

#print("Resultado a si se le puede cambiar la tierra (Amapola): ", amapola_roja.cambiarTierra())
#print("¿Está disponible? (Amapola): ", amapola_roja.isAvailable(amapola_roja.tipo))
