#Programación funcional
#Encriptamiento
""""
def encriptar(mensaje, posiciones):
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    resultado =''
    for letra in mensaje:
        if letra in alfabeto:
            posicion = alfabeto.index(letra)
            nueva_posicion = (posicion + posiciones) % 27
            resultado += alfabeto[nueva_posicion]
        else:
            resultado += letra
            return resultado
        print(encriptar('hola mundo', 3)) 
        
"""


""""
def encriptar(mensaje, posiciones):
    abecedario = 'abcdefghijklmnñopqrstuvwxyz '
    resultado = ''
    for letra in mensaje:
        if letra in abecedario:
            indice = abecedario.index(letra)
            nuevo_indice = (indice + posiciones) % 27
            resultado += abecedario[nuevo_indice]
        else:
            resultado += letra
    return resultado

def a_invertido(texto):
    return texto[::-1]

def a_mayuscula(texto):
    return texto.upper()

texto_usuario = input("Ingrese una frase: ")

mensaje_modificado = a_invertido(a_mayuscula(encriptar(texto_usuario, 3)))

print("Mensaje encriptado:", mensaje_modificado)
"""

""""
def login():
    def validar_usuario():
        
        usuarios= {"user1": "pass1", "user2": "pass2", "user3": "pass3"}
        if username in usuarios and usuarios[username] == password:
            return True
        else:
            return False
        
    
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    
    if validar_usuario():
        print("Bienvenido, usuario: ")
    else:
        print("Usuario o contraseña incorrectos")
    
    login()
"""
""""
def sumar(n1, n2):
    return n1 + n2

x = sumar
print(type(x))
print(x(3,2))
print(sumar(3,9))
print(x)
print(sumar)

"""

""""
def function_A():
    def function_b():
        return "Hola, soy función B"
    return function_b()

x = function_A()
print(x)
print(type(x))
print(x())

"""
""""
def potencia(n):
    def eleva(x):
        return x ** n
    return eleva

cuadrado = potencia(2)
cubo = potencia (3)
print(cuadrado(5))
print (cubo(2))

pot = potencia (int(input("Ingrese la potencia deseada: ")))

print(pot(int(input("Ingrese la base que quiere elevar: "))))

"""

""""
def transformar_lista(lista, funcion):
  nueva_lista = []
  for numero in lista:
    nueva_lista.append(funcion(numero))
  return nueva_lista

def siguiente(numero):
  return numero + 1

def anterior(numero):
  return numero - 1

def duplicar(numero):
  return numero * 2

opciones = {
  1: siguiente,
  2: anterior,
  3: duplicar
}

def main():
  # Pedir la cantidad de números
  while True:
    cantidad = input("Ingrese la cantidad de números que necesita: ")
    if cantidad.isdigit() and int(cantidad) > 0:
      cantidad = int(cantidad)
      break
    else:
      print("La cantidad debe ser un número entero positivo. Por favor, inténtelo de nuevo.")

  # Pedir la lista por medio de un input
  while True:
    lista_input = input(f"Ingrese la lista de {cantidad} números separados por espacios: ")
    lista = list(map(int, lista_input.split()))
    if len(lista) == cantidad:
      break
    else:
      print(f"La lista debe tener exactamente {cantidad} números. Por favor, inténtelo de nuevo.")

  print(f"Lista original: {lista}")

  print("Seleccione una opción:")
  print("1. Siguiente")
  print("2. Anterior")
  print("3. Duplicar")

  opcion = int(input("Ingrese el número de la opción: "))

  if opcion in opciones:
    funcion = opciones[opcion]
    lista_transformada = transformar_lista(lista, funcion)
    print(f"Lista transformada: {lista_transformada}")
  else:
    print("Opción inválida")

if __name__ == "__main__":
  main()
  
  """
import re

def validar_contraseña(contraseña):
  patrón = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!#$%&'()*+-./:;<=>?@[\]^_`{|}~]).{6,}$"
  return bool(re.match(patrón, contraseña))

def crear_usuarios():
  usuarios = []
  for i in range(3):
    nombre = input(f"Ingrese el nombre del usuario {i+1}: ")
    while True:
      contraseña = input(f"Ingrese la contraseña para el usuario {i+1} : ")
      if validar_contraseña(contraseña):
        break
      print("La contraseña no cumple con los requisitos de seguridad. Por favor, inténtelo de nuevo.")
    usuarios.append({"nombre": nombre, "contraseña": contraseña})
  return usuarios

def iniciar_sesion(usuarios):
  nombre = input("Ingrese su nombre de usuario: ")
  contraseña = input("Ingrese su contraseña: ")
  for usuario in usuarios:
    if usuario["nombre"] == nombre and usuario["contraseña"] == contraseña:
      print("Inicio de sesión exitoso!")
      return True
  print("Nombre de usuario o contraseña incorrectos.")
  return False

def main():
  usuarios = crear_usuarios()
  print("Usuarios creados:")
  for usuario in usuarios:
    print(f"Nombre: {usuario['nombre']}, Contraseña: {usuario['contraseña']}")
  while True:
    print("\n1. Iniciar sesión")
    print("2. Salir")
    opcion = input("Ingrese su opción: ")
    if opcion == "1":
      if iniciar_sesion(usuarios):
        break
    elif opcion == "2":
      print("Hasta luego!")
      break
    else:
      print("Opción inválida. Por favor, inténtelo de nuevo.")

if __name__ == "__main__":
  main()