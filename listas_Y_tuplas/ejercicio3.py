lista=["quimica","historia","matematicas","licantropia"]
nota =""
notas=[]
for i in lista:
    nota=(input("que nota sacaste en "+i+" es: "))
    notas.append(nota)
    print(nota)
for i in range(len(lista)):
    print("tu nota en",lista[i], "es de",notas[i])    