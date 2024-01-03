numero=int(input("ingresa un numero: "))
cadena=""
for i in range(numero):
    if (i+1)%2 != 0 :
        cadena=cadena+","+str((i+1))
y=cadena.split(",")
for i in range(len(y)):
    print(y[i+1])       
      