numeros=str(input("ingresa tu numero de celular: "))
if numeros[0]=="+" :
    corte1=numeros[3:]
    if corte1[0]=="-":
        corte1=corte1[1:]
        signo=True
    else:
        signo=False

if signo==True:    
    numero=len(corte1)
    corte2=corte1[:(numero-3)]
else:
    numero=len(corte1)
    corte2=corte1[:(numero-2)]
print(corte2)