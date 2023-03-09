# Prog1 - UFCG
# Rayane Bezerra da Silva
# Verificando se um numero é igual ao seu vizinho.

numeros = input().split()

vizinhos = 0

for i in range(len(numeros)-1):
    if int(numeros[i]) == int(numeros[ i + 1]):
        vizinhos += 1
        
print(vizinhos)
