estrato=int(input("Ingrese su estrato: "))
edad=int(input("Ingrese su edad: "))
matricula=int(input("Ingrese el coste de su matricula: "))

if estrato ==1 and edad <18:
    resultado= matricula *0.20
    print("La matricula con el descuento es de: " , resultado)
elif estrato ==1 and edad >18:
    resultado= matricula *0.15
    print("La matricula con el descuento es de: " , resultado)
elif estrato ==2 and edad <18:
    resultado= matricula *0.10
    print("La matricula con el descuento es de: " , resultado)
elif estrato ==2 and edad >=18:
    resultado= matricula *0.5
    print("La matricula con el descuento es de: " , resultado)
