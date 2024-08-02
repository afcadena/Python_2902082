class Figura(object):
    def calcular_area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return 3.14159 * self.radio * self.radio

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    
    def calcular_area(self):
        return self.lado * self.lado

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return (self.base * self.altura) / 2

# Comprobación de las diferentes clases
circulo = Circulo(5)
print("Área del círculo:", circulo.calcular_area())

cuadrado = Cuadrado(4)
print("Área del cuadrado:", cuadrado.calcular_area())

triangulo = Triangulo(3, 6)
print("Área del triángulo:", triangulo.calcular_area())
