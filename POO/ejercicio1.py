class estudiante:
    def __init__(self, nombre, edad, grado) :
        self.nombre=nombre
        self.edad=edad
        self.grado=grado
    def estudiar(self):
        print("el estudiante "+self.nombre+" esta estudiando: ")
usuario=estudiante(input("ingresa el nombre del estudiante: "),
                   input("ingresa la edad del estudiante: "),
                   input("ingresa el grado del estudiante: "))
usuario.estudiar()