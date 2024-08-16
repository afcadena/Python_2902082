class Vivienda:
    def __init__(self, nombre_comprador, documento_identidad, correo, celular):
        self.__nombre_comprador = nombre_comprador
        self.__documento_identidad = documento_identidad
        self.__correo = correo
        self.__celular = celular

    def get_nombre_comprador(self):
        return self.__nombre_comprador

    def get_documento_identidad(self):
        return self.__documento_identidad

    def get_correo(self):
        return self.__correo

    def get_celular(self):
        return self.__celular

class Casa(Vivienda):
    def __init__(self, nombre_comprador, documento_identidad, correo, celular, direccion, barrio, localidad, valor_casa):
        super().__init__(nombre_comprador, documento_identidad, correo, celular)
        self.__direccion = direccion
        self.__barrio = barrio
        self.__localidad = localidad
        self.__valor_casa = max(0, valor_casa) 
        self.__matricula = self.__valor_casa * 0.05
        self.__impuesto = self.__matricula * 0.02

    def get_direccion(self):
        return self.__direccion

    def get_barrio(self):
        return self.__barrio

    def get_localidad(self):
        return self.__localidad

    def get_valor_casa(self):
        return self.__valor_casa

    def get_matricula(self):
        return self.__matricula

    def get_impuesto(self):
        return self.__impuesto

class Apartamento(Vivienda):
    def __init__(self, nombre_comprador, documento_identidad, correo, celular, n_apartamento, bloque, piso, valor_apartamento):
        super().__init__(nombre_comprador, documento_identidad, correo, celular)
        self.__n_apartamento = n_apartamento
        self.__bloque = bloque
        self.__piso = piso
        self.__valor_apartamento = valor_apartamento
        self.__impuestos = self.calcular_impuestos()

    def calcular_impuestos(self):
        if 1 <= self.__piso <= 3:
            return self.__valor_apartamento * 0.03
        elif 4 <= self.__piso <= 8:
            return self.__valor_apartamento * 0.10
        elif self.__piso >= 9:
            return self.__valor_apartamento * 0.20
        else:
            return 0

    def get_n_apartamento(self):
        return self.__n_apartamento

    def get_bloque(self):
        return self.__bloque

    def get_piso(self):
        return self.__piso

    def get_valor_apartamento(self):
        return self.__valor_apartamento

    def get_impuestos(self):
        return self.__impuestos

def validar_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("El valor debe ser un número positivo.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

def positivo_decimal(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("El valor debe ser un número positivo.")
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")

def venta_casa():
    while True:
        try:
            valor = float(input("Ingrese el valor de la casa (entre 300 y 600 millones): "))
            if 300 <= valor <= 600:
                return valor
            else:
                print("El valor debe estar entre 300 y 600 millones.")
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")

def venta_apartamento():
    return positivo_decimal("Ingrese el valor del apartamento: ")

def mostrar_registros(viviendas):
    if not viviendas:
        print("No hay registros para mostrar.")
    for i, vivienda in enumerate(viviendas):
        print(f"\nRegistro {i+1}:")
        if isinstance(vivienda, Casa):
            print("\n--- Información de la Casa ---")
            print(f"Nombre del comprador: {vivienda.get_nombre_comprador()}")
            print(f"Documento de identidad: {vivienda.get_documento_identidad()}")
            print(f"Correo electrónico: {vivienda.get_correo()}")
            print(f"Celular: {vivienda.get_celular()}")
            print(f"Dirección: {vivienda.get_direccion()}")
            print(f"Barrio: {vivienda.get_barrio()}")
            print(f"Localidad: {vivienda.get_localidad()}")
            print(f"Valor de la casa: {vivienda.get_valor_casa()} millones")
            print(f"Matricula: {vivienda.get_matricula()} millones")
            print(f"Impuesto: {vivienda.get_impuesto()} millones")
        
        elif isinstance(vivienda, Apartamento):
            print("\n--- Información del Apartamento ---")
            print(f"Nombre del comprador: {vivienda.get_nombre_comprador()}")
            print(f"Documento de identidad: {vivienda.get_documento_identidad()}")
            print(f"Correo electrónico: {vivienda.get_correo()}")
            print(f"Celular: {vivienda.get_celular()}")
            print(f"Número del apartamento: {vivienda.get_n_apartamento()}")
            print(f"Bloque: {vivienda.get_bloque()}")
            print(f"Piso: {vivienda.get_piso()}")
            print(f"Valor del apartamento: {vivienda.get_valor_apartamento()} millones")
            print(f"Impuestos: {vivienda.get_impuestos()} millones")

def main():
    viviendas = []

    while True:
        print("\n1. Ingresar nueva vivienda")
        print("2. Ver registros")
        print("3. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            tipo_vivienda = input("¿Desea ingresar una casa o un apartamento? (casa/apartamento): ").strip()
            
            nombre_comprador = input("Ingrese el nombre del comprador: ")
            documento_identidad = validar_positivo("Ingrese el documento de identidad: ")
            correo = input("Ingrese el correo electrónico: ")
            celular = validar_positivo("Ingrese el número de celular: ")

            if tipo_vivienda == 'casa':
                direccion = input("Ingrese la dirección de la casa: ")
                barrio = input("Ingrese el barrio: ")
                localidad = input("Ingrese la localidad: ")
                valor_casa = venta_casa()
                casa = Casa(nombre_comprador, documento_identidad, correo, celular, direccion, barrio, localidad, valor_casa)
                viviendas.append(casa)
            
            elif tipo_vivienda == 'apartamento':
                n_apartamento = validar_positivo("Ingrese el número del apartamento: ")
                bloque = validar_positivo("Ingrese el bloque: ")
                piso = validar_positivo("Ingrese el piso: ")
                valor_apartamento = venta_apartamento()
                apartamento = Apartamento(nombre_comprador, documento_identidad, correo, celular, n_apartamento, bloque, piso, valor_apartamento)
                viviendas.append(apartamento)

            else:
                print("Tipo de vivienda no válido. Por favor, ingrese 'casa' o 'apartamento'.")

        elif opcion == '2':
            mostrar_registros(viviendas)

        elif opcion == '3':
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()
