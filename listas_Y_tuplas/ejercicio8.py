palabra= input("ingrese una palabra: ")
if palabra=="".join(reversed(palabra)):
    print("es un palindromo")
else:
    print("no es palindromo")