pizza=input("desea una pizza vegana? resonda 'si' o 'no' \n")
ingredientes=""
if pizza=="si":
    ingredientes=input("elija uno de estos ingredientes: Pimiento, tofu \n")
    pizza="vegana"
elif pizza=="no":
    ingredientes=input("elija uno de estos ingredientes: Peperoni, Jamón y Salmón \n")
    pizza="no vegana"
else:
    print("error")
if ingredientes!="":
    print("usted elijio la pizza",pizza,"con el ingrediente agregado:",ingredientes)            