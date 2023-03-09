# Prog1 - UFCG
# Rayane Bezerra da Silva
# Calculando quantos dias uma pessoa precisa para perder uma determinada quantidade de quilos.

quilos = float(input())
tempo = int(input())
calorias_consumidas = int(input())

calorias_perdidas = 2000 - calorias_consumidas
dieta_dias = (quilos * 7700) / ((tempo * 900) + calorias_perdidas)

print(f'Você precisará de {dieta_dias :.2f} dias de dieta')
