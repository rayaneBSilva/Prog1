# Prog1 -UFCG
# Rayane Bezerra da Silva
# Calculando o valor da corrente eletrica.

tensao_1 = int(input())
resistencia_1 = int(input())
tensao_2 = int(input())
resistencia_2 = int(input())
tensao_3 = int(input())
resistencia_3 = int(input())

corrente_1 = tensao_1 / resistencia_1
corrente_2 = tensao_2 / resistencia_2
corrente_3 = tensao_3 / resistencia_3

maior = 0
maior_corrente = 0
mensagem = ''

if corrente_1 >= corrente_2 and corrente_1 >= corrente_3:
    maior = 1
    maior_corrente = corrente_1
elif corrente_2 >= corrente_3:
    maior = 2
    maior_corrente = corrente_2
else:
    maior = 3
    maior_corrente = corrente_3


if maior_corrente < 0.001:
    mensagem= f"maior corrente: {maior_corrente * 1000000:.2f} µA"
elif maior_corrente < 1:
    mensagem= f"maior corrente: {maior_corrente * 1000:.2f} mA"
else:
    mensagem= f"maior corrente: {maior_corrente:.2f} A"

print(f"condutor com maior corrente: {maior}")
print(mensagem)

