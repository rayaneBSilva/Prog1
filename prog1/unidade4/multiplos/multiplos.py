# Prog1 -UFCG
# Rayane Bezerra da Silva
# Encontrando números vizinhos que são múltiplos.

sequencia = input().split()
fator = int(input())

quantidade_pares = 0
pares = []

for i in range(len(sequencia)-1):
    if (int(sequencia[i]) * fator) == int(sequencia[i + 1 ]) or (int(sequencia[i]) / fator ) == int(sequencia[ i + 1]):
        quantidade_pares += 1
        pares.append(f'{sequencia[i]} {sequencia[i + 1]}')
   
print(f'{quantidade_pares} par(es)')     

for par in pares:
    print(par)
    
