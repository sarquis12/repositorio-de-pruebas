ingreso=(input("escribir palabras en español con su traduccion separados por dos puntos, y si desea colocar otra palabra coloque una coma: "))
diccionario={}
for i in ingreso.split(","):
    x=i.split(":")
    diccionario[x[0]]=x[1]
print(diccionario)    
frase= input("introduce frase a traducir")
frase_traducida=""
for i in frase.split(" "):
    if i in diccionario:
        frase_traducida+=" "+diccionario[i]
    else:
        frase_traducida+=" "+i
print(frase_traducida)