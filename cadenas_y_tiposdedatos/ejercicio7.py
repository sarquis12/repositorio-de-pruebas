correo_usuario=input("ecsribe tu correo electronico: ")
correo_guardado = str("")
i=int(0)
while correo_usuario[i] != "@":   
    correo_guardado= correo_guardado + correo_usuario[i] 
    i=i+1
correo_guardado=correo_guardado+"@ceu.es"
print(correo_guardado)

print(correo_usuario[:correo_usuario.find('@')] + '@ceu.es')