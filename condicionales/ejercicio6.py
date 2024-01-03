nombre=input("ingresa nombre: ")
sexo=input("ingresa sexo: ")
primer="abcdefghijklm"
segundo="nñopqrstuwxyz"
marca=False
if sexo=="m":
    for i in range(len(primer)):
        if nombre[0]==segundo[i]:
            print("eres del primer grupo")
            marca=True
    if marca==False:
        print("eres del segundo grupo")    
elif sexo=="f":
    for i in range(len(primer)):
        if nombre[0]==primer[i]:
            print("eres del primer grupo")
            marca=True
    if marca==False:
        print("eres del segundo grupo") 
else:
    print("ingresaste mal el genero")              