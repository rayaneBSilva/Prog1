# Prog1 -UFCG
# Rayane Bezerra da Silva
# Calculando média de pares.

N = int(input())

numeros_pares = []
inteiros = []
pares = 0
soma = 0
acima_da_media = 0

for c in range(N):
    numeros = input()
    inteiros.append(numeros)
    if int(numeros) % 2 == 0:
        numeros_pares.append(numeros)
        pares += 1
        
for i in numeros_pares:
    soma += int(i)
    media_pares = soma / pares
  

for inteiro in inteiros:
    if int(inteiro) > media_pares:
        acima_da_media += 1


print(f'média dos pares: {media_pares:.1f}')
print(f'acima da média: {acima_da_media}')

