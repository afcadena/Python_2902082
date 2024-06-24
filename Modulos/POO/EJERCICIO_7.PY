class Estudiante:
    def __init__(self, nombre, nota1, nota2):
        self.__nombre = nombre
        self.__nota1 = self.__validar_nota(nota1)
        self.__nota2 = self.__validar_nota(nota2)
    
    def __validar_nota(self, nota):
        if nota < 0 or nota > 5:
            raise ValueError("Las notas deben estar entre 0 y 5.")
        return nota
    
    def obtener_nota_promedio(self):
        return (self.__nota1 + self.__nota2) / 2
    
    def mostrar_informacion(self):
        promedio = self.obtener_nota_promedio()
        print(f"Información del estudiante:")
        print(f"Nombre: {self.__nombre}")
        print(f"Nota 1: {self.__nota1}")
        print(f"Nota 2: {self.__nota2}")
        print(f"Nota promedio: {promedio}")
    
    # Getters y setters para los atributos privados
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_nota1(self):
        return self.__nota1
    
    def set_nota1(self, nota1):
        self.__nota1 = self.__validar_nota(nota1)
    
    def get_nota2(self):
        return self.__nota2
    
    def set_nota2(self, nota2):
        self.__nota2 = self.__validar_nota(nota2)

def main():
    try:
        nombre = input("Ingrese el nombre del estudiante: ")
        nota1 = float(input("Ingrese la nota 1 del estudiante (0 a 5): "))
        nota2 = float(input("Ingrese la nota 2 del estudiante (0 a 5): "))
        
        estudiante = Estudiante(nombre, nota1, nota2)
        
        # Mostrar la información del estudiante
        estudiante.mostrar_informacion()
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
