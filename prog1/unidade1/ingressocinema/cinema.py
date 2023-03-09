# Prog1 - UFCG
# Rayane Bezerra da Silva
# Calculando  o preço de um ingresso.

adulto = int(input())
criança = int(input())
ingresso = float(input())

valor_total = (adulto * ingresso) + (criança * (ingresso/2))
print(f'Total: R$ {valor_total :.2f}')