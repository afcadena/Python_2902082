class Factura:
    def __init__(self, codigo_producto, nombre_producto, cantidad, valor_unitario):
        self.__codigo_producto = codigo_producto
        self.__nombre_producto = nombre_producto
        self.__cantidad = cantidad
        self.__valor_unitario = valor_unitario
        self.__valor_total = cantidad * valor_unitario

    def obtener_factura(self):
        subtotal = self.__valor_total
        iva = subtotal * 0.19
        total = subtotal + iva
        return {
            "Código del Producto": self.__codigo_producto,
            "Nombre del Producto": self.__nombre_producto,
            "Cantidad": self.__cantidad,
            "Valor Unitario": self.__valor_unitario,
            "Subtotal": subtotal,
            "IVA": iva,
            "Total": total
        }

    @staticmethod
    def capturar_informacion():
        productos = []
        for i in range(3):
            codigo_producto = input(f"Introduce el código del producto {i+1}: ")
            nombre_producto = input(f"Introduce el nombre del producto {i+1}: ")
            cantidad = int(input(f"Introduce la cantidad del producto {i+1}: "))
            valor_unitario = float(input(f"Introduce el valor unitario del producto {i+1}: "))
            productos.append(Factura(codigo_producto, nombre_producto, cantidad, valor_unitario))
        return productos

def imprimir_facturas(productos):
    print(f"{'Código':<15}{'Nombre':<25}{'Cantidad':<10}{'Valor Unitario':<15}{'Subtotal':<10}{'IVA':<10}{'Total':<10}")

    subtotal_acumulado = 0
    iva_acumulado = 0
    total_acumulado = 0

    for producto in productos:
        factura = producto.obtener_factura()
        print(f"{factura['Código del Producto']:<15}{factura['Nombre del Producto']:<25}{factura['Cantidad']:<10}{factura['Valor Unitario']:<15}{factura['Subtotal']:<10}{factura['IVA']:<10}{factura['Total']:<10}")
        subtotal_acumulado += factura["Subtotal"]
        iva_acumulado += factura["IVA"]
        total_acumulado += factura["Total"]

    print("\n")
    print(f"Subtotal Acumulado: {subtotal_acumulado}")
    print(f"IVA Acumulado: {iva_acumulado}")
    print(f"Total Acumulado: {total_acumulado}")


productos = Factura.capturar_informacion()
imprimir_facturas(productos)