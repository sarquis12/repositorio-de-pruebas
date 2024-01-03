diccionario={}
x="si"
while x!="no":
    dato=input("que dato quieres ingresar?:")
    diccionario[str(dato)]=input("cual es tu "+dato+": ")
    print(diccionario)
    x=input("quieres agregar otro dato? si/no: ")
    