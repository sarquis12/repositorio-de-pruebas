compras={}
x="si"
precio_total=0
while x!="no":
    articulo=input("que articulo quieres comprar?:")
    precio=input("cual es su precio?:")
    if len(articulo)<15:
        articulo+=" "*(15-len(articulo))
    compras[articulo]=(precio)
    precio_total+=int(precio)
    x=input("quieres agregar otro articulo? si/no: ")
compras["total          "]=precio_total
for i in compras:
    print(i,compras[(i)])