vector1=([1,2,3,4],[4,5,6,3])
vector2=([1,0],[0,1],[1,1],[2,2])
acumulador=0
resultado=""
for i in vector1:
    for x in (range(len(vector2[0]))):
        for y in range(len(vector2)):
            acumulador+=i[y]*vector2[y][x]
        resultado=resultado+" "+str(acumulador)
        acumulador=0
    
    resultado=resultado+"\n"   
print (resultado)       
          

        
        
    
    
    
