def calcular_porcentaje(sexo, total_estudiantes):
    """
    Calcula el porcentaje de estudiantes de un género específico.

    Args:
        sexo (str): El género de los estudiantes ('h' para hombres, 'm' para mujeres).
        total_estudiantes (int): El total de estudiantes en el grupo.

    Returns:
        float: El porcentaje de estudiantes del género especificado.
    """
    if sexo == 'h':
        return (hombres / total_estudiantes) * 100
    elif sexo == 'm':
        return (mujeres / total_estudiantes) * 100
    else:
        return 0

# Solicitar datos al usuario
hombres = int(input("Ingrese el número de hombres en el grupo: "))
mujeres = int(input("Ingrese el número de mujeres en el grupo: "))

# Calcular el total de estudiantes
total_estudiantes = hombres + mujeres

# Calcular el porcentaje de hombres y mujeres
porcentaje_hombres = calcular_porcentaje('h', total_estudiantes)
porcentaje_mujeres = calcular_porcentaje('m', total_estudiantes)

# Imprimir resultados
print(f"Porcentaje de hombres: {porcentaje_hombres:.2f}%")
print(f"Porcentaje de mujeres: {porcentaje_mujeres:.2f}%")
