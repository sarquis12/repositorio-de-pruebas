print("escribe los 6 numeros ganadores de la loteria")
ganadores=[]
numeros=0
for i in range (6):
    numeros=int(input("numero  ganador "+str(i+1)+" :"))
    ganadores.append(numeros)
ganadores.sort()
print(ganadores)    