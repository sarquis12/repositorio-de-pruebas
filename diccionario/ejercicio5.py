diccionario={'Matemáticas': 6, 'Física': 4, 'Química': 5}
x=0
for i in diccionario:
    print(i,"tiene",diccionario[i],"creditos")
    x+=diccionario[i]
print("su numero total de creditos es de:",x)