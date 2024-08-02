def calcular_comision(ventas, porcentaje_comision):
    """
    Calcula el monto de comisión basado en el número de ventas y el porcentaje de comisión.

    Args:
        ventas (int): Número de ventas realizadas en el mes.
        porcentaje_comision (float): Porcentaje de comisión sobre las ventas.

    Returns:
        float: El monto de comisión ganado.
    """
    comision = ventas * porcentaje_comision
    return comision

# Solicitar datos al usuario
sueldo_base = float(input("Ingrese el sueldo base del vendedor: "))
ventas_mes = int(input("Ingrese el número de ventas realizadas en el mes: "))
porcentaje_comision = 0.10  # 10% de comisión sobre las ventas

# Calcular la comisión y el total del sueldo mensual
monto_comision = calcular_comision(ventas_mes, porcentaje_comision)
total_sueldo_mensual = sueldo_base + monto_comision

# Imprimir resultados
print(f"El monto de comisión por las {ventas_mes} ventas realizadas es: ${monto_comision:.2f}")
print(f"El total del sueldo mensual, incluyendo comisiones, es: ${total_sueldo_mensual:.2f}")
