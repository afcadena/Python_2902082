
class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo=0):
        self.__numero_cuenta = numero_cuenta
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, cantidad):
        try:
            cantidad = float(cantidad)
            if cantidad > 0:
                self.__saldo += cantidad
                print(f"Depósito de ${cantidad} realizado \nSaldo actual: ${self.__saldo}")
            else:
                print("La cantidad a depositar debe ser mayor que cero")
        except ValueError:
            print("Error: Por favor, ingrese un número válido para la cantidad")

    def retirar(self, cantidad):
        try:
            cantidad = float(cantidad)
            if cantidad > 0:
                if self.__saldo >= cantidad:
                    self.__saldo -= cantidad
                    print(f"Retiro de ${cantidad} realizado \nSaldo actual: ${self.__saldo}")
                else:
                    print("Saldo insuficiente")
            else:
                print("La cantidad a retirar debe ser mayor que cero.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido para la cantidad.")

    def transferir(self, cantidad, otra_cuenta):
        try:
            cantidad = float(cantidad)
            if cantidad > 0:
                if self.__saldo >= cantidad:
                    self.__saldo -= cantidad
                    otra_cuenta.depositar(cantidad)
                    print(f"Transferencia de ${cantidad} realizada a la cuenta de {otra_cuenta.__titular}. 
                          Saldo actual: ${self.__saldo}")
                else:
                    print("Saldo insuficiente para realizar la transferencia.")
            else:
                print("La cantidad a transferir debe ser mayor que cero.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido para la cantidad.")

    def mostrar_saldo(self):
        print(f"\nSaldo de la cuenta de {self.__titular}: ${self.__saldo}")


def ingresar_datos_cuenta():
    numero_cuenta = input("Ingrese el número de cuenta: ")
    titular = input("Ingrese el titular de la cuenta: ")
    saldo = input("Ingrese el saldo inicial de la cuenta: ")
    try:
        saldo = float(saldo)
    except ValueError:
        print("Error: Por favor, ingrese un número válido para el saldo inicial.")
        saldo = 0.0  # Asignamos un saldo inicial seguro en caso de error
    return numero_cuenta, titular, saldo


print("Datos de la cuenta 1:")
numero_cuenta1, titular1, saldo1 = ingresar_datos_cuenta()
cuenta1 = CuentaBancaria(numero_cuenta1, titular1, saldo1)

print("\nDatos de la cuenta 2:")
numero_cuenta2, titular2, saldo2 = ingresar_datos_cuenta()
cuenta2 = CuentaBancaria(numero_cuenta2, titular2, saldo2)

opcion = "0"
while opcion != "5":
    print("\nBienvenido al Banco:")
    print("1. Mostrar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Transferir")
    print("5. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        cuenta1.mostrar_saldo()
    elif opcion == "2":
        cantidad = input("Ingrese la cantidad a depositar en la cuenta 1: ")
        cuenta1.depositar(cantidad)
    elif opcion == "3":
        cantidad = input("Ingrese la cantidad a retirar de la cuenta 1: ")
        cuenta1.retirar(cantidad)
    elif opcion == "4":
        cantidad = input("Ingrese la cantidad a transferir de la cuenta 1 a la cuenta 2: ")
        cuenta1.transferir(cantidad, cuenta2)
    elif opcion == "5":
        print("Gracias por utilizar nuestros servicios. ¡Hasta luego!")
    else:
        print("Opción inválida. Por favor, selecciona una opción válida (1/2/3/4/5).")




# Trabajo 2

class Figura:
    def calcular_area(self):
        pass  


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        area = 3.1416 * self.radio ** 2  # Usamos un valor aproximado de pi
        return area


class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    
    def calcular_area(self):
        area = self.lado ** 2
        return area

# Subclase Triangulo que hereda de Figura
class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        area = (self.base * self.altura) / 2
        return area

# Cálculos directos sin menú
def calcular_area_figura(opcion, params):
    if opcion == 1:
        radio = params
        circulo = Circulo(radio)
        return circulo.calcular_area()
    elif opcion == 2:
        lado = params
        cuadrado = Cuadrado(lado)
        return cuadrado.calcular_area()
    elif opcion == 3:
        base, altura = params
        triangulo = Triangulo(base, altura)
        return triangulo.calcular_area()
    else:
        print("Opción no válida.")

# Ejemplo de uso:
opcion = int(input("Seleccione la figura para calcular el área:\n"
                   "1. Círculo\n"
                   "2. Cuadrado\n"
                   "3. Triángulo\n"
                   "Ingrese su opción (1/2/3): "))

if opcion in [1, 2, 3]:
    if opcion == 1:
        radio = float(input("Ingrese el radio del círculo: "))
        area = calcular_area_figura(opcion, radio)
        print(f"El área del círculo con radio {radio} es: {area}")
    elif opcion == 2:
        lado = float(input("Ingrese el lado del cuadrado: "))
        area = calcular_area_figura(opcion, lado)
        print(f"El área del cuadrado con lado {lado} es: {area}")
    elif opcion == 3:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = calcular_area_figura(opcion, [base, altura])
        print(f"El área del triángulo con base {base} y altura {altura} es: {area}")
else:
    print("Opción no válida. Por favor, seleccione una opción válida (1/2/3).")

