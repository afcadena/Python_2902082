#POO Encapsulamiento Metodos privados 
class Banco:
    def __init__(self,nombre,n_cuenta,celular,direccion,email,saldo):
        self.set_nombre(nombre)
        self.set_n_cuenta(n_cuenta)
        self.set_celular(celular)
        self.set_direccion(direccion)
        self.set_email(email)
        self.set_saldo(saldo)
        
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def get_n_cuenta(self):
        return self._n_cuenta
    def set_n_cuenta(self, n_cuenta):
        self._n_cuenta = n_cuenta
    
    def get_celular(self):
        return self._celular
    def set_celular(self, celular):
        self._celular = celular
    
    def get_direccion(self):
        return self._direccion
    def set_direccion(self, direccion):
        self._direccion = direccion
    
    def get_email(self):
        return self._email
    def set_email(self, email):
        self._email = email
    
    def get_saldo(self):
        return self._saldo
    def set_saldo(self, saldo):
        self._saldo = saldo
        

banco = Banco("Sin Nombre", "Sin Cuenta", "Sin Celular", "Sin Dirección", "Sin Email", 0.0)


n_nombre = input("Introduce el nombre: ")
n_n_cuenta = input("Introduce el número de cuenta: ")
n_celular = int(input("Introduce el número de celular: "))
n_direccion = input("Introduce la dirección: ")
n_email = input("Introduce el email: ")
n_saldo = float(input("Introduce el saldo: "))

banco.set_nombre(n_nombre)
banco.set_n_cuenta(n_n_cuenta)
banco.set_celular(n_celular)
banco.set_direccion(n_direccion)
banco.set_email(n_email)
banco.set_saldo(n_saldo)


print(f"---------------------------------------------------------")
print(f"Nombre: {banco.get_nombre()}")
print(f"Número de Cuenta: {banco.get_n_cuenta()}")
print(f"Celular: {banco.get_celular()}")
print(f"Dirección: {banco.get_direccion()}")
print(f"Email: {banco.get_email()}")
print(f"Saldo: {banco.get_saldo()}")

    
    
    