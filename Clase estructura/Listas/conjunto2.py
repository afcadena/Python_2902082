num=int(input("ingrese el rango de los cuadrados que desea "))
cuadrado= {}

for num in range(1,num+1):
   
    cuadrado[num] = num**2
for num, valor in cuadrado.items():
    print("%d->%d" %(num,valor))