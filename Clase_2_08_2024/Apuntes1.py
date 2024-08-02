class Persona:
    def __init__(self, nombre, documento, direccion):
        self.set_nombre(nombre)
        self.set_documento(documento)
        self.set_direccion(direccion)
    
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre
        
    def get_documento(self):
        return self._documento
    
    def set_documento(self, documento):
        self._documento = documento
        
    def get_direccion(self):
        return self._direccion
    
    def set_direccion(self, direccion):
        self._direccion = direccion
    
    def mostrar_persona(self):
        return f"Nombre: {self.get_nombre()}, \nDocumento: {self.get_documento()}, \nDirección: {self.get_direccion()}"

class Empleado(Persona):
    def __init__(self, nombre, documento, direccion, codigo, cargo, empresa, sueldo):
        super().__init__(nombre, documento, direccion)
        self.set_codigo(codigo)
        self.set_cargo(cargo)
        self.set_empresa(empresa)
        self.set_sueldo(sueldo)
    
    def get_codigo(self):
        return self._codigo
    
    def set_codigo(self, codigo):
        self._codigo = codigo
    
    def get_cargo(self):
        return self._cargo
    
    def set_cargo(self, cargo):
        self._cargo = cargo
    
    def get_empresa(self):
        return self._empresa
    
    def set_empresa(self, empresa):
        self._empresa = empresa
    
    def get_sueldo(self):
        return self._sueldo
    
    def set_sueldo(self, sueldo):
        self._sueldo = sueldo
    
    def mostrar_empleado(self):
        return (self.mostrar_persona() + 
                f", \nCódigo de Empleado: {self.get_codigo()}, \nCargo: {self.get_cargo()}, \nEmpresa: {self.get_empresa()}, \nSueldo: {self.get_sueldo()}")

class Estudiante(Persona):
    def __init__(self, nombre, documento, direccion, codigo, programa, trimestre):
        super().__init__(nombre, documento, direccion)
        self.set_codigo(codigo)
        self.set_programa(programa)
        self.set_trimestre(trimestre)
    
    def get_codigo(self):
        return self._codigo
    
    def set_codigo(self, codigo):
        self._codigo = codigo
    
    def get_programa(self):
        return self._programa
    
    def set_programa(self, programa):
        self._programa = programa
    
    def get_trimestre(self):
        return self._trimestre
    
    def set_trimestre(self, trimestre):
        self._trimestre = trimestre
    
    def mostrar_estudiante(self):
        return (self.mostrar_persona() + 
                f", \nCódigo de Estudiante: {self.get_codigo()}, \nPrograma: {self.get_programa()}, \nTrimestre: {self.get_trimestre()}")


print("Ingresar datos para Empleado:")
nombre = input("Nombre: ")
documento = input("Documento: ")
direccion = input("Dirección: ")
codigo_empleado = input("Código de Empleado: ")
cargo = input("Cargo: ")
empresa = input("Empresa: ")
sueldo = input("Sueldo: ")

empleado = Empleado(nombre, documento, direccion, codigo_empleado, cargo, empresa, sueldo)
print("\nDatos del Empleado:")
print(empleado.mostrar_empleado())

print("\n---------------------------------------------------------------------------------------------------------------------")


print("\nIngresar datos para Estudiante:")
nombre = input("Nombre: ")
documento = input("Documento: ")
direccion = input("Dirección: ")
codigo_estudiante = input("Código de Estudiante: ")
programa = input("Programa: ")
trimestre = input("Trimestre: ")

estudiante = Estudiante(nombre, documento, direccion, codigo_estudiante, programa, trimestre)
print("\nDatos del Estudiante:")
print(estudiante.mostrar_estudiante())
