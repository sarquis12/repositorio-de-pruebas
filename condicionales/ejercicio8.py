nota=float(input("ingresa la nota del usuario: "))
nota=round(nota, 1)
if nota==0:
    print("inaceptable, tu pago extra es de 0")
elif nota==0.4:
    print("aceptable, tu pago extra es de:",0.4*2400) 
else:
    print("meritorio, tu pago extra sera de:",nota*2400)       