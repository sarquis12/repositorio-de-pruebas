numero=int(input("ingresa numero: "))
x=0
guardar=""
for i in range(1, numero+1):
    while x !=i:        
        guardar=str(1+x*2)+guardar
        x=x+1        
    print(guardar)       