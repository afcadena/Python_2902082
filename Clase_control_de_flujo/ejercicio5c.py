amarillo=0
rosa=0
roja=0
verde=0
azul=0
carro=1
while (carro == 1 ) :
    placa=int(input("Ingrese el último digito de la placa: "))
    if placa == 1 or placa == 2 :
        amarillo +1
    elif placa == 3 or placa == 4 :
        rosa +1
    elif placa == 5 or placa == 6 :
        roja +1
    elif placa == 7 or placa == 8 :
        verde +1
    elif placa == 9 or placa == 0 :
        azul +1
    print()    
    