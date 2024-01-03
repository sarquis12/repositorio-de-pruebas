abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
multiplos_3=[]
for i in range(1,len(abecedario)):
    if i%3==0:
        multiplos_3.append(abecedario[i-1])
for i in multiplos_3:
    abecedario.remove(i)  
print(abecedario)          
        
