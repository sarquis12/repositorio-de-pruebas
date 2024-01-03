lista=["quimica","historia","matematicas","licantropia"]
lista_dupla=["quimica","historia","matematicas","licantropia"]
for i in lista_dupla :    
    nota=int(input("nota de la materia "+ i+":"))
    if nota>6:
        lista.remove(i)
print("tienes que repertir:",lista)    