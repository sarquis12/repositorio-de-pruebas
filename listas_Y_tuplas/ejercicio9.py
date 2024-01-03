palabra=input("ingresa palabra: ")
vocales=["a","e","i","o","u"]
contador=0
for i in vocales:
    contador=0
    for x in range(len(palabra)):
        if i==palabra[x]:
            contador+=1
    print("la cantidad de",i  ,"que tiene ",palabra,"es",contador)