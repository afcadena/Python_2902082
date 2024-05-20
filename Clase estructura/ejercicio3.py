mi_lista=[1,2,3,4,5,6,7,8,9,12,3,4,4,5,6,7,54,3,2,4,6,8,9]
mi_lista1=int(input("ingrese un numero: "))
contador=0
for elemento in mi_lista:
    if mi_lista1==elemento:
        contador+=1
    print(f"{mi_lista1} aparece {contador} veces en la lista")    