edad=int(input("ingresa edad: "))
ingresos=int(input("ingresa ingresos mensuales: "))
if edad>16:
    if ingresos>=1000:
        print("tienes que tributar")
    else:
        print("no tienes que tributar")
else:
    print("no tienes que tributar")

if edad>16 and ingresos>=1000:
    print("tienes que tributar") 
else:
    print("no tienes que tributar")               