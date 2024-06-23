def agregar_una_vez(lista, el):
    if el in lista:
        print(f"Error: Imposible añadir elementos duplicados => {el}.")
    else:
        lista.append(el)
    print("Gracias por usar este programa")

# Función principal
def main():
    lista = []

    while True:
        try:
            entrada = input("Ingrese el elemento que desea agregar (o 'q' para salir): ")
            if entrada.lower() == 'q':
                break
            el = int(entrada)
            agregar_una_vez(lista, el)
            print("Lista actualizada:", lista)
        except ValueError:
            print("Error: Por favor ingrese un número entero válido.")

    print("Programa terminado correctamente")

if __name__ == "__main__":
    main()
