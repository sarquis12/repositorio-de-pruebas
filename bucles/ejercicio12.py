palabra=input("ingresa una palabra: ")
letra=input("ingresa una letra: ")
contador=0
for i in range(len(palabra)):
    if palabra[i]==letra:
        contador=contador+1
print("la cantidad de veces que se repite la letra",letra,"fue:",contador)