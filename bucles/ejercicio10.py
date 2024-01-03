numero=int(input("dame un numero: "))
primo=True
if numero>1:    
    for i in range(2, numero-1):
        if numero % i == 0 and numero !=2:        
            primo=False        
else:
    primo=False
if primo==False:
    print("no es primo")
else:
    print("es primo")
i=2
while numero%i:
    i+=1
if numero==i:
    print("es primooooo")
else:
    print("no es primoooo")            