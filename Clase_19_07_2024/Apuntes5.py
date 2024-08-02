from abc import ABC, abstractmethod

class Juego(ABC):
    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def mostrar_puntaje(self):
        pass

    @abstractmethod
    def terminar(self):
        pass

class JuegoSimple(Juego):
    def __init__(self):
        self.puntaje = 0

    def iniciar(self):
        print("Juego iniciado")
        input("Presione cualquier tecla para continuar...")
        self.puntaje = 0

    def mostrar_puntaje(self):
        print(f"Puntaje actual: {self.puntaje}")

    def terminar(self):
        print("Juego terminado")
        self.mostrar_puntaje()

    def ganar_puntos(self, puntos):
        self.puntaje += puntos

def menu():
    juego = JuegoSimple()
    juego.iniciar()
    
    while True:
        print("\nSeleccione una opción:")
        print("1. Mostrar puntaje")
        print("2. Ganar puntos")
        print("3. Terminar")
        
        opcion = input("Ingrese el número de la opción: ")
        
        if opcion == "1":
            juego.mostrar_puntaje()
        elif opcion == "2":
            puntos = int(input("Ingrese la cantidad de puntos a ganar: "))
            juego.ganar_puntos(puntos)
        elif opcion == "3":
            juego.terminar()
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()