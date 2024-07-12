# externo.py

import Grafico.Ejercicio_1
import Borde.Ejercicio_3
import Relleno.Ejercicio_2

# Llamadas a funciones del módulo Grafico
Grafico.Ejercicio_1.Cuadrado()
Grafico.Ejercicio_1.Rectangulo()
Grafico.Ejercicio_1.Rombo()
Grafico.Ejercicio_1.Triangulo()

# Llamadas a funciones del módulo Borde
Borde.Ejercicio_3.perimetro_cuadrado()
Borde.Ejercicio_3.perimetro_rectangulo()
Borde.Ejercicio_3.perimetro_triangulo()
Borde.Ejercicio_3.perimetro_rombo()

# Para Relleno, debes proporcionar los argumentos necesarios
lado_cuadrado = 4
base_rectangulo = 5
altura_rectangulo = 6
base_triangulo = 7
altura_triangulo = 8
diagonal_menor_rombo = 3
diagonal_mayor_rombo = 4

# Llamadas a funciones del módulo Relleno
print(f"Área del cuadrado: {Relleno.Ejercicio_2.area_cuadrado(lado_cuadrado)}")
print(f"Área del rectángulo: {Relleno.Ejercicio_2.area_rectangulo(base_rectangulo, altura_rectangulo)}")
print(f"Área del triángulo: {Relleno.Ejercicio_2.area_triangulo(base_triangulo, altura_triangulo)}")
print(f"Área del rombo: {Relleno.Ejercicio_2.area_rombo(diagonal_menor_rombo, diagonal_mayor_rombo)}")
