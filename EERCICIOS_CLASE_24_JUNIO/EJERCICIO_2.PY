import math

def area_cuadrado(lado):
    
    return lado ** 2

def area_rectangulo(base, altura):

    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_rombo(diagonal_menor, diagonal_mayor):
    
    return (diagonal_menor * diagonal_mayor) / 2

if __name__ == "__main__":
    lado_cuadrado = float(input("Ingrese el lado del cuadrado: "))
    base_rectangulo = float(input("Ingrese la base del rectángulo: "))
    altura_rectangulo = float(input("Ingrese la altura del rectángulo: "))
    base_triangulo = float(input("Ingrese la base del triángulo: "))
    altura_triangulo = float(input("Ingrese la altura del triángulo: "))
    diagonal_menor_rombo = float(input("Ingrese la diagonal menor del rombo: "))
    diagonal_mayor_rombo = float(input("Ingrese la diagonal mayor del rombo: "))

    area_cuadrado_calculada = area_cuadrado(lado_cuadrado)
    area_rectangulo_calculada = area_rectangulo(base_rectangulo, altura_rectangulo)
    area_triangulo_calculada = area_triangulo(base_triangulo, altura_triangulo)
    area_rombo_calculada = area_rombo(diagonal_menor_rombo, diagonal_mayor_rombo)
    
    print(f"Área del cuadrado: {area_cuadrado_calculada}")
    print(f"Área del rectángulo: {area_rectangulo_calculada}")
    print(f"Área del triángulo: {area_triangulo_calculada}")
    print(f"Área del rombo: {area_rombo_calculada}")
