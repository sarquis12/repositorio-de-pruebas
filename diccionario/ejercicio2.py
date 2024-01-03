frutas={"banana":10,"manzana":15,"pera":20,"naranja":12}
fruta=input("ingrsa fruta: ")
kilos=input("cuantos kilos quieres? ")
bandera=False
for i in frutas:
    if i==fruta:
        print(kilos, "kilos de",i,"cuestan",frutas[i]*int(kilos))
        bandera=True
if bandera==False:print("NO SE ENCUENTRA LA FRUTA QUE BUSCA") 