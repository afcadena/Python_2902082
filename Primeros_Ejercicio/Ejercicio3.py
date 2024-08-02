def calcular_descuento(total_compra, porcentaje_descuento):
    """
    Calcula el monto de descuento basado en el total de la compra y el porcentaje de descuento.

    Args:
        total_compra (float): El total de la compra.
        porcentaje_descuento (float): El porcentaje de descuento a aplicar.

    Returns:
        float: El monto del descuento.
    """
    descuento = total_compra * (porcentaje_descuento / 100)
    return descuento

# Solicitar datos al usuario
total_compra = float(input("Ingrese el total de la compra: "))
porcentaje_descuento = 15  # Porcentaje de descuento del 15%

# Calcular el monto del descuento
monto_descuento = calcular_descuento(total_compra, porcentaje_descuento)

# Calcular el total a pagar después del descuento
total_a_pagar = total_compra - monto_descuento

# Imprimir resultados
print(f"El monto de descuento aplicado es: ${monto_descuento:.2f}")
print(f"El total a pagar después del descuento es: ${total_a_pagar:.2f}")
