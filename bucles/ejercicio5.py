print("\n")
inversion = float(input ("cantidad a invertir: "))
interes = float(input ("igrese el interes anual: "))
años = int(input ("cantidad de años: "))
interes=interes/100
for i in range(años):
    inversion=inversion+inversion*interes
    print("el año",i+1,"la cantidad obtenida fue de:",inversion)
