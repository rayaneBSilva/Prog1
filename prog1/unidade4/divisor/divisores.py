# Prog1 - UFCG
# Rayane Bezerra da Silva
# Encontrando divisores de um número.

numero = int(input())

for divisor in range(1, numero):
    if numero % divisor == 0:
        print(divisor)
    
