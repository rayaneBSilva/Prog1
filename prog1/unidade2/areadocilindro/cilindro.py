#Prog1 - UFCG
#Rayane Bezerra da Silva
#Calculando a área do cilindro.

import math

print('Cálculo da Superfície de um Cilindro')
print('---')

diametro = float(input('Medida do diâmetro? '))
altura = float(input('Medida da altura? '))

area_da_base = (math.pi * (diametro/2) ** 2)
area_lateral = (2 * math.pi)* (diametro/2) * altura
area_final = (2 * area_da_base) + area_lateral

print('---')

print(f'Área calculada: {area_final :.2f}')

