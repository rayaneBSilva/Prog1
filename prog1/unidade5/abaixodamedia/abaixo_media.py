# Prog1 - UFCG
# Rayane Bezerra da Silva
# Calculando numeros abaixo da média.

soma = 0
media = 0
contador = 0
abaixo_da_media = []
posicao = []


while True:
    numero = input()
    if numero == 'fim': break
    soma += int(numero)
    contador += 1
    media = soma / contador 
    abaixo_da_media.append(int(numero))
    posicao.append(contador)
    
print(f'{media :.2f}')

for i in range(len(abaixo_da_media)):
    if abaixo_da_media[i] < media:
        print(f'{posicao[i]} {abaixo_da_media[i]}')
