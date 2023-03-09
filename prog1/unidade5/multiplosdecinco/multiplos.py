# Prog1 -UFCG
# Rayane Bezerra da Silva
# Calculando multiplos de 5 que são pares.

limite = int(input())

numero = 1

while numero < limite:
    if numero % 5 == 0 and numero % 2 == 0: 
        print(numero)
    numero += 1
