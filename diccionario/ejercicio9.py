seguir="si"
facturas={1:200,2:250,3:400,5:200}
pregunta=""
total=0
while seguir=="si":
    pregunta=input("escribe ' agregar' para agregar una factura o 'pagar' para pagar ")
    if pregunta=="agregar":
        factura=int(input("numero de factura"))
        costo=input("costo de la factura")
        facturas[factura]=costo
    elif pregunta=="pagar":
        factura=int(input("ingresa la factura a pagar"))
        del facturas[factura]
    seguir=input("si quieres seguir escribe si")
for i in facturas:
    total+=int(facturas[i])
print("el total a pagar sumando todas las facturas es de:",total)
    
    
    
     
    
    