diccionario = {"19":"1500"}
factura_a_pagar=""
def añadir ():
    numero_factura = input("ingrese nro de factura: ")
    precio = (input ("ingrese el precio: ")) 
    diccionario[numero_factura]=precio
    print (diccionario)
def pagar():
    factura_a_pagar= input ("ingrese la factura a pagar: ")
    del diccionario [factura_a_pagar]
    print (diccionario)
seguir = True




def seleccion (opcion):
    if opcion=="añadir":
        añadir()
    elif opcion=="pagar":            
        pagar ()
    elif opcion=="terminar":
        global seguir 
        seguir=False
while seguir:
   a =input ("que quieres hacer? ")
   seleccion(a) 
