renta=int(input("cuanto pagas de renta: "))
if renta<10000:
    print("tu impositivo es de: 5%")
elif 10000<=renta<20000:
    print("tu impositivo es de: 15%")
elif 20000<=renta<35000:
    print("tu impositivo es de: 20%")
elif 35000<=renta<60000:
    print("tu impositivo es de: 30%")
else:  
    print("tu impositivo es de: 45%")         