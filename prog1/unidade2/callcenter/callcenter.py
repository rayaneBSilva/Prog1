# Prog1 -UFCG
# Rayane Bezerra da Silva

sequencia = input().split()

elemento = 0
posição = 0
existe = False


for i in range(len(sequencia)-1):
    if int(sequencia[i]) > int(sequencia[ i + 1]):    
        elemento = sequencia[ i + 1]           
        posição = i + 1
        existe = True
        break
    else:
        existe = False
        
if existe == True:
    print(f'{elemento} (posição {posição})')
else:
    print('Sem traíra.')
    
        

    


