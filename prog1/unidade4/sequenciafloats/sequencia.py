# Prog1 - UFCG
# Rayane Bezerra da Silva
# Imprindo sequencia de numeros floats.

inicio = 15.2
final = -8.0
delta = -1.5

repeticoes = int((final - inicio) / delta)

for i in range(repeticoes):
    numero = inicio + i * delta
    print(f'{numero :.1f}')
