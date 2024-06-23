class Estudiante:
    def __init__(self, nombre, nota1, nota2):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
    
    def obtener_nota_promedio(self):
        return (self.nota1 + self.nota2) / 2
    
    def mostrar_informacion(self):
        promedio = self.obtener_nota_promedio()
        print(f"Información del estudiante:")
        print(f"Nombre: {self.nombre}")
        print(f"Nota 1: {self.nota1}")
        print(f"Nota 2: {self.nota2}")
        print(f"Nota promedio: {promedio}")

# Función principal
def main():
    # Crear un estudiante
    nombre = input("Ingrese el nombre del estudiante: ")
    try:
        nota1 = float(input("Ingrese la nota 1 del estudiante: "))
        nota2 = float(input("Ingrese la nota 2 del estudiante: "))
        
        estudiante = Estudiante(nombre, nota1, nota2)
        
        # Mostrar la información del estudiante
        estudiante.mostrar_informacion()
    except ValueError:
        print("Error: Por favor ingrese notas válidas (números).")

if __name__ == "__main__":
    main()
