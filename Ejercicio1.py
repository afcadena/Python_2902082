def calcular_interes(capital, tasa):
    """
    Calcula el interés ganado después de un mes.
    
    Args:
        capital (float): El capital inicial.
        tasa (float): La tasa de interés mensual en porcentaje.
        
    Returns:
        float: El interés ganado después de un mes.
    """
    interes = capital * (tasa / 100)
    return interes

# Ejemplo de uso
capital = float(input("Ingrese el capital a invertir: "))
tasa = 2  # Tasa de interés mensual del 2%
interes_ganado = calcular_interes(capital, tasa)
print(f"El interés ganado después de un mes será: ${interes_ganado:.2f}")
