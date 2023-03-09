# Prog1 - UFCG
# Rayane Bezerra da Silva
# Calculando a  hipotenusa.

import math

cateto_1 = float(input('Cateto 1? '))
cateto_2 = float(input('Cateto 2? '))

hipotenusa = math.sqrt((cateto_1 ** 2) + (cateto_2 ** 2))
print(f'Hipotenusa: {hipotenusa :.2f}')
