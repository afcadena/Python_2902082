def calcular_calificacion_final(promedio_parciales, calificacion_examen, calificacion_trabajo):
    """
    Calcula la calificación final en la materia de Algoritmos.

    Args:
        promedio_parciales (float): Promedio de las tres calificaciones parciales.
        calificacion_examen (float): Calificación del examen final.
        calificacion_trabajo (float): Calificación del trabajo final.

    Returns:
        float: La calificación final en la materia de Algoritmos.
    """
    calificacion_final = (promedio_parciales * 0.55) + (calificacion_examen * 0.30) + (calificacion_trabajo * 0.15)
    return calificacion_final

# Solicitar datos al usuario
parcial1 = float(input("Ingrese la calificación del primer parcial: "))
parcial2 = float(input("Ingrese la calificación del segundo parcial: "))
parcial3 = float(input("Ingrese la calificación del tercer parcial: "))
examen_final = float(input("Ingrese la calificación del examen final: "))
trabajo_final = float(input("Ingrese la calificación del trabajo final: "))

# Calcular el promedio de los tres parciales
promedio_parciales = (parcial1 + parcial2 + parcial3) / 3

# Calcular la calificación final
calificacion_final = calcular_calificacion_final(promedio_parciales, examen_final, trabajo_final)

# Imprimir resultado
print(f"La calificación final en la materia de Algoritmos es: {calificacion_final:.2f}")
