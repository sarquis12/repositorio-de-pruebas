base_datos={"44331163":{"nombre":"elias","direccion":"pasaje fray mocho","telefono":"3624074266","correo":"eliass_sarquiss@hotmail.com","preferente":True}}
datos={"nombre":"","direccion":"","telefono":"","correo":"","preferente":""}
dni=0
seguir="si"
ingreso=""
while seguir=="si":
    opcion= input("escriba la opcion que quiera realizar: \n añadir cliente=1 \n eliminar cliente=2 \n mostrar cliente=3 \n listar todos los clientes=4 \n listar clientes preferentes=5 \n terminar=6 \n")
    if opcion=="1":
        dni=input("ingrese el dni del cliente a ingresar: ")
        for i in datos :
            if i=="preferente":
                ingreso=input("si el cliente es preferente escriba 'si'y si no es preferente escriba 'no':")
                if ingreso=="si":
                    ingreso=True
                else:
                    ingreso=False
            else:
                ingreso=input("ingrese "+i+":")
            datos[i]=ingreso
        base_datos[dni]=datos
    elif opcion=="2":
        dni=input("ingrese un cliente a eliminar: ")
        del base_datos[dni]
    elif opcion=="3":
        dni=input("ingrese cliente a mostrar: ")
        if dni in base_datos:
            print(base_datos[dni]["nombre"])
            input()
        else:
            print("no se encontro ese cliente")
            input()              
    elif opcion=="4":
        for i in base_datos:
            print(base_datos[i]["nombre"])
        input()
               
    elif opcion=="5":
        for i in base_datos:
            if base_datos[i]["preferente"]==True:
                print(base_datos[i]["nombre"])  
        input()                    
    elif opcion=="6":seguir="no"        
    else:
        print("ingresaste numero equivocado")
        input()