# Prog1 - UFCG
# Rayane Bezerra da Silva
# Calculando as raízes das equações de segundo grau.

import math

a = float(input())
b = float(input())
c = float(input())

delta = (b ** 2) -4 * a * c

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a) 
    print(f'x1 = {x1:.2f}')
    print(f'x2 = {x2:.2f}')
elif delta == 0:
    x = (-b + math.sqrt(delta)) / ( 2 * a)
    print(f'x = {x:.2f}')
else:
    print('sem raizes reais')
