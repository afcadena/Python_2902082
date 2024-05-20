
precios_frutas = { "manzana": 1.5, "pera": 2.0, "platano": 1.0,"naranja": 0.8, "fresa":2.7}

  
while True:
    
    nombre_fruta = input("Ingrese el nombre de la fruta: ").lower()

    if nombre_fruta in precios_frutas:
      
      cantidad = float(input("Ingrese la cantidad vendida: "))

      precio_total = precios_frutas[nombre_fruta] * cantidad

    
      print(f"El precio total de la {nombre_fruta} es: {precio_total:.2f}")

    else:
      
      print(f"La fruta '{nombre_fruta}' no existe en el inventario.")

    otra_venta = input("¿Desea realizar otra venta? (s/n): ").lower()

    if otra_venta != "s":
        break
