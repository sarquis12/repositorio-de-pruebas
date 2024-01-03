lista=[50, 75, 46, 22, 80, 65, 8]
mayor=lista[0]
menor=lista[0]
for i in lista:
    for x in lista:
        if i>=x :           
            if i>=mayor:                
                mayor=i
print(mayor)          
for i in lista:
    for x in lista:
        if i<=x :           
            if i<=menor:                
                menor=i     
print(menor)  

lista.sort ()
print("elemento menor:",lista[0]) 
print("elemento menor:",lista[-1])       