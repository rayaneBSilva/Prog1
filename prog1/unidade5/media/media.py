# Prog1 -UFCG
# Rayane Bezerra da Silva
# calculando média

contador = 0
soma = 0
posicao = []
valores = []

while True:
    valor = input()
    if valores == 'fim': break
    contador += 1
    soma += int(valores)
    media = soma / contador
    posicao.append(contador)
    valores.append(valor)
    
    print(media)
print(posicao)

    
    
    