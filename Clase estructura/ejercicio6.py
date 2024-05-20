cantidad=int(input("numeros de elementos de la serie: "))
ant=1
print(ant)
act=1
print(act)
for x in range (1, cantidad+1):
    pos=act+ant
    ant=act
    act=pos
    print(act)


