class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

class Cuenta:
    def __init__(self, numero, tipo, saldo):
        self.numero = numero
        self.tipo = tipo
        self.saldo = saldo

class Banco:
    _instancia = None

    def __new__(cls, nombre):
        if cls._instancia is None:
            cls._instancia = super(Banco, cls).__new__(cls)
            cls._instancia.nombre = nombre
            cls._instancia.clientes = []
        return cls._instancia

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def adicionar_cliente(self, nombre, cedula):
        cliente = Cliente(nombre, cedula)
        self.clientes.append(cliente)
        return cliente

    def ver_info_clientes(self):
        info_clientes = []
        for cliente in self.clientes:
            for cuenta in cliente.cuentas:
                info_clientes.append({
                    'Cedula': cliente.cedula,
                    'Nombre': cliente.nombre,
                    'Numero de cuenta': cuenta.numero,
                    'Tipo': cuenta.tipo,
                    'Saldo': cuenta.saldo
                })
        return info_clientes

    def total_saldo_cuentas_ahorros(self):
        total = 0
        for cliente in self.clientes:
            for cuenta in cliente.cuentas:
                if cuenta.tipo == 'Ahorro':
                    total += cuenta.saldo
        return total

    def total_saldo_cuentas_corrientes(self):
        total = 0
        for cliente in self.clientes:
            for cuenta in cliente.cuentas:
                if cuenta.tipo == 'Corriente':
                    total += cuenta.saldo
        return total

# Ejemplo de uso
banco = Banco('Banco Central')

# Cambiar nombre del banco
banco.cambiar_nombre('Banco Nacional')

# Adicionar clientes
cliente1 = banco.adicionar_cliente('Juan Pérez', '12345678')
cliente2 = banco.adicionar_cliente('Ana Gómez', '87654321')

# Agregar cuentas a los clientes
cliente1.agregar_cuenta(Cuenta('001', 'Ahorro', 1500))
cliente1.agregar_cuenta(Cuenta('002', 'Corriente', 500))
cliente2.agregar_cuenta(Cuenta('003', 'Ahorro', 2000))
cliente2.agregar_cuenta(Cuenta('004', 'Corriente', 800))

# Ver información de clientes
info_clientes = banco.ver_info_clientes()
for info in info_clientes:
    print(info)

# Ver total de saldos en cuentas de ahorros y corrientes
print(f'Total saldo en cuentas de ahorro: {banco.total_saldo_cuentas_ahorros()}')
print(f'Total saldo en cuentas corrientes: {banco.total_saldo_cuentas_corrientes()}')
