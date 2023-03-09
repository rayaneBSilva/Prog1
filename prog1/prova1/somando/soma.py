# Prog1 -UFCG
# Rayane Bezerra da Silva
# Matricula - 120210483
# Calculando soma dos extremos.

n = int(input())


numeros = []
contador = 0
soma = 0
media = 0
soma_extremos = 0


for c in range(n):
    numero = int(input())
    numeros.append((numero))
    soma += numero
    contador += 1
    media = soma / contador 
    
for i in range(len(numeros)-1,-1,-1):
    soma_extremos += numeros[i]
    if numeros[i] >= media: break 

print(soma_extremos)
