# Prog1 - UFCG
# Rayane Bezerra da Silva
# Encontrando o perimetro e a área, de um quadrado na circuferencia.

import math

lado = float(input())
raio = (lado * (2 ** 0.5)) / 2
perimetro = 2 * math.pi * raio
area = math. pi * (raio ** 2) 

print(f'Perimetro: {perimetro :.5f}')
print(f'Área: {area :.5f}')
