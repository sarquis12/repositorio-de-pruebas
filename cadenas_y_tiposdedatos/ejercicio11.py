nombre=str(input("ingrese producto: "))
precio=float(input("ingrese precio de producto: "))
cantidad=str(input("ingrese cantidad del producto: "))
if int(len(cantidad))<3:
    a=str(cantidad).zfill(3)
cadena = nombre+"#"+str(round(precio,2)).zfill(7)+"#"+str(a)+"#"+str(round(precio*int(cantidad),2)).zfill(6)
print (cadena)
