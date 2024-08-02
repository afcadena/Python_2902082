frutos_recolectados = float(input("Ingrese la cantidad de frutos recolectados: "))
frutos_producidos = float(input("Ingrese la cantidad de frutos producidos en total: "))

indice_cosecha = (frutos_recolectados / frutos_producidos) * 100
print("El índice de cosecha es:", indice_cosecha, "%")
