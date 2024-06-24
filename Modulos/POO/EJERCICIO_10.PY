from tabulate import tabulate

class Estudiante5:
    Institucion = "Sena CGMLTI"
    Cantidad_Estudiantes = 0
    lista_estudiantes = []

    def __init__(self, nombre, nota1, nota2):
        self.__nombre = nombre
        self.__nota1 = self.__validar_nota(nota1)
        self.__nota2 = self.__validar_nota(nota2)
        self.Conteo_Estudiantes()
        Estudiante5.lista_estudiantes.append(self)  # Agregar el estudiante a la lista

    def __validar_nota(self, nota):
        if nota < 0 or nota > 5:
            raise ValueError("Las notas deben estar entre 0 y 5.")
        return nota

    @property
    def nombre(self):
        return self.__nombre

    @property
    def nota1(self):
        return self.__nota1

    @property
    def nota2(self):
        return self.__nota2
    
    @classmethod
    def cambiar_institucion(cls, nueva_institucion):
        cls.Institucion = nueva_institucion

    def obtener_nota_promedio(self):
        return (self.__nota1 + self.__nota2) / 2

    def __str__(self):
        return f"Nombre del Estudiante: {self.__nombre} \n  Nota Promedio: {self.obtener_nota_promedio()} \n Institucion: {Estudiante5.Institucion}"
    
    @classmethod
    def obtener_cantidad_estudiantes(cls):
        return cls.Cantidad_Estudiantes
    
    def Conteo_Estudiantes(self):
        Estudiante5.Cantidad_Estudiantes += 1
    
    @classmethod
    def clasificar_nota(cls, nota):
        if 0.0 <= nota <= 2.9:
            return "BAJA"
        elif 3.0 <= nota <= 3.9:
            return "MEDIA"
        elif 4.0 <= nota <= 4.5:
            return "ALTA"
        elif 4.6 <= nota <= 5.0:
            return "SOBRESALIENTE"
        else:
            return "N/A"
    
    @classmethod
    def ver_escala(cls):
        # Definir la escala de calificación
        tabla_escala = [
            ["Nota", "Escala"],
            ["0 - 2.9", "BAJA"],
            ["3 - 3.9", "MEDIA"],
            ["4 - 4.5", "ALTA"],
            ["4.6 - 5", "SOBRESALIENTE"],
        ]
        print("Rango de notas")
        print(tabulate(tabla_escala, headers="firstrow", tablefmt="fancy_grid"))
        
        # Crear la tabla de estudiantes con sus clasificaciones
        tabla_estudiantes = [["Nombre", "Nota 1", "Nota 2", "Nota Promedio", "Escala"]]
        for estudiante in cls.lista_estudiantes:
            nombre = estudiante.nombre
            nota1 = estudiante.nota1
            nota2 = estudiante.nota2
            promedio = estudiante.obtener_nota_promedio()
            escala = cls.clasificar_nota(promedio)
            tabla_estudiantes.append([nombre, nota1, nota2, promedio, escala])
        
        # Mostrar la tabla de estudiantes usando tabulate
        print("\nTabla de calificaciones de los estudiantes:")
        print(tabulate(tabla_estudiantes, headers="firstrow", tablefmt="fancy_grid"))

estudiante1 = Estudiante5("Carlos", 4.5, 5.0)
estudiante2 = Estudiante5("Pedro", 3.5, 3.5)
estudiante3 = Estudiante5("Mario", 1.5, 2.0)
estudiante4 = Estudiante5("Carla", 4.5, 5.0)
estudiante5 = Estudiante5("Carolina", 3.0, 4.0)

Estudiante5.ver_escala()