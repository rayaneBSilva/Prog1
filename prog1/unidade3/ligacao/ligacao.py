# Prog1 - UFCG
# Rayane Bezerra da Silva
# Calculando o preço de uma ligação.

minutos = int(input())

ligaçao_preço = 0

if minutos <= 3:
   ligaçao_preço = 1 + (minutos * 0.50)
else:
    if minutos >= 5:
      ligaçao_preço = (( minutos // 5) * 3.00 ) + (( minutos % 5) * 0.70) + 1.0
    else:
      ligaçao_preço = (minutos * 0.70) + 1

print(f'R$ {ligaçao_preço :.2f}')
