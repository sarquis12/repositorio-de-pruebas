libreria={}
poder_total=float(0)
nombre_campeon=""
class personaje():
    def crearPersonaje ():
        for i in range(2):
            nombre=input("ingresa nombre del personaje " +str(i+1)+":")
            poder=input("ingresa nivel de poder de personaje "+str(i+1)+":")           
            libreria[i]=[nombre, poder]
    def fusion(self,numero_poder):
        numero_poder=int(numero_poder)
        if numero_poder<100:
            numero_poder=numero_poder*2
        elif numero_poder>=100 and poder_total<500:
            numero_poder=(numero_poder/10)**2  
        elif numero_poder>500:
            numero_poder=numero_poder*100
        print("la fusion se llama"+"y su nivel de poder es:"+str(numero_poder))
          
x=personaje
x.crearPersonaje()
for i in libreria:
    poder_total =poder_total+ int(libreria[i][1])
    for x in range(3):
        nombre_campeon += libreria[i][0][x]
print(poder_total,nombre_campeon)  
x.fusion (str(poder_total))
        