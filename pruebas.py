diccionario={"elias":"sarquis","emanuel": "correa"}
oracion=input("")
oracion=oracion.split(" ")
x=""
for i in oracion:
    if i in diccionario:
        x+=diccionario[i]+" "
    else:
        x+=i+" "
print (x)