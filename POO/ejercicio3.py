class animal:
    def comer():
        return("come")
        
class mamifero(animal):
    def amamantar():
        return("amamanta")
class ave(animal):
    def volar():
        return("vuela")
class murcielago(mamifero,ave):
    pass
x=murcielago
print(murcielago.comer())