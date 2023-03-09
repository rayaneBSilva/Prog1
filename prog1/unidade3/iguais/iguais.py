# Prog1 - UFCG
# Rayane Bezerra da Silva
# Calculando quantos numeros sao iguais.

numero_1 = int(input())
numero_2 = int(input())
numero_3 = int(input())

numero_iguais = 0

if numero_1 == numero_2 == numero_3:
    numero_iguais += 3
elif numero_1 == numero_2 or numero_3 == numero_2 or numero_1 == numero_3:
    numero_iguais += 2
    
print(numero_iguais)