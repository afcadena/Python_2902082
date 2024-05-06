años = int(input("Ingrese la cantidad de años que lleva: "))
sueldo = float(input("Ingrese su su sueldo mensual: "))

if años >=0 and años <=1:
    resultado = sueldo * 0.05
    print("El sueldo es de: " , resultado)
elif años >=1 and años <=2:
    resultado= sueldo * 0.07
    print("El sueldo es de: " , resultado)
elif años >=2 and años <=5:
    resultado= sueldo * 0.10
    print("El sueldo es de: " , resultado)
elif años >=5 and años <=10:
    resultado= sueldo * 0.15
    print("El sueldo es de: " , resultado)
elif años >=10:
    resultado= sueldo * 0.20
    print("El sueldo es de: " , resultado)
