def perimetro_cuadrado(lado):
    return lado * 4

def perimetro_rectangulo(largo, ancho):
    return 2 * (largo + ancho)

def perimetro_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3

def perimetro_rombo(lado):
    return lado * 4

if __name__ == "__main__":
    lado_cuadrado = float(input("Ingrese el lado del cuadrado: "))
    print(f"Perímetro del cuadrado: {perimetro_cuadrado(lado_cuadrado)}")

    largo_rectangulo = float(input("Ingrese el largo del rectángulo: "))
    ancho_rectangulo = float(input("Ingrese el ancho del rectángulo: "))
    print(f"Perímetro del rectángulo: {perimetro_rectangulo(largo_rectangulo, ancho_rectangulo)}")

    lado1_triangulo = float(input("Ingrese el lado 1 del triángulo: "))
    lado2_triangulo = float(input("Ingrese el lado 2 del triángulo: "))
    lado3_triangulo = float(input("Ingrese el lado 3 del triángulo: "))
    print(f"Perímetro del triángulo: {perimetro_triangulo(lado1_triangulo, lado2_triangulo, lado3_triangulo)}")

    lado_rombo = float(input("Ingrese el lado del rombo: "))
    print(f"Perímetro del rombo: {perimetro_rombo(lado_rombo)}")
