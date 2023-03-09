# Prog1 -UFCG
# Rayane Bezerra da Silva
# Utilizando o teorema de herão para calcular área de triângulo.

import math

N = int(input())

areas = []
maiores = 0
areas_maiores = []
repetiçoes = 0
media = 0

for c in range(N):
    repetiçoes += 1
    triangulos = input().split()
    a = float(triangulos[0])
    b = float(triangulos [1])
    c = float(triangulos [2])
    s = (a + b + c) / 2
    area = math.sqrt( s * ( s - a ) * ( s - b ) * ( s - c))
    areas.append(area)

        
for i in range(len(areas)):
    print(f'Área {i + 1}: {areas[i]:.2f}')
    if areas[i] > 100.00:
        maiores += 1
        areas_maiores.append(areas[i])
        
    
for maior in areas_maiores:
    media += maior / maiores

print(f'Número maiores: {maiores}, área média: {media:.2f}')
