class Vehiculo:
    def Movimiento(self):
        pass
    
class Avion(Vehiculo):
    def Movimiento(self):
        print("Vuela")

class Tren(Vehiculo): 
    def Movimiento(self):
        print("Corre")

class Barco(Vehiculo):
    def Movimiento(self):
        print("Navega")

class Moto(Vehiculo):
    def Movimiento(self):
        print("Veloz")
        
        
def Mostrar_Movimiento(vehiculo):
    if isinstance (vehiculo, Vehiculo):
        vehiculo.Movimiento()
    else:
        print("No funciona")
        
aerio = Avion()
Tranvia = Tren()
agua = Barco()
Carretera = Moto()
#otro_objeto = object()

Mostrar_Movimiento(aerio)
Mostrar_Movimiento(Tranvia)
Mostrar_Movimiento(agua)
Mostrar_Movimiento(Carretera)
#Mostrar_Movimiento(otro_objeto)