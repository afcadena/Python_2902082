dict={}
cadena= input("dame una cadena: ")
for caracter in cadena:
    if caracter in dict:
        dict[caracter]+=1
    else:
        dict[caracter]=1
        
for campo,valor in dict.items():
    print(campo,"->",valor)