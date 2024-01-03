class persona:
    def __init__(self, nombre, edad) :
        self.nombre=nombre
        self.edad=edad
        
class estudiante(persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado=grado
    def imprimir(self):
        print(self.grado)  

x=estudiante("alan","15","2do")
x.imprimir()