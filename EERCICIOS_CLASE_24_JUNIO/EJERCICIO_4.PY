lista = [3, 5, 6, 8]

while True:
    try:
        pos = int(input("Ingrese la posición del elemento que desea obtener: "))
        if pos < 0 or pos >= len(lista):
            raise IndexError
        print(f"El valor en la posición {pos} es {lista[pos]}")
        break
    except ValueError:
        print("La posición ingresada no es válida. Debe ser un número entero.")
    except IndexError:
        print(f"La posición {pos} no existe en la lista. Debe ser un número entre 0 y {len(lista) - 1}.")

print("Programa terminado correctamente")
