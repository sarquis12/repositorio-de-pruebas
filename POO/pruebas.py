libreria={}
poder_total=float(0)
nombre_campeon=""
class personaje():
    def __init__(self, nombre_personaje, poder_personaje) :
        self.nombre=nombre_personaje
        self.poder=poder_personaje
    def crear(self):
        self.nombre=input("ingresa nombre del personaje :")
        self.poder=input("ingresa nivel de poder de personaje :")           
        libreria[self.nombre]=self.poder
    def fusion(self):
        self.poder=int(0)
        self.nombre=""
        for i in libreria:
            self.poder =self.poder+ int(libreria[i])
            for x in range(3):
                self.nombre+=i[x]
        if self.poder<100:
            self.poder=self.poder*2
        elif self.poder>=100 and self.poder<500:
            self.poder=(self.poder/10)**2  
        elif self.poder>500:
            self.poder=self.poder*100
        print("la fusion se llama "+self.nombre+" y su nivel de poder es:"+str(self.poder)+"!!!!!!")      
x=personaje("","")
for i in range (2):
    x.crear()
  
x.fusion()

