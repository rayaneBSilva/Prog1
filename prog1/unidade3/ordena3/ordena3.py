# Prog1 - UFCG
# Rayane Bezerra da Silva
# Ordenando numeros.

numero_1 = int(input())
numero_2 = int(input())
numero_3 = int(input())

if numero_1 >= numero_2 and numero_1 >= numero_3:
    if numero_2 >= numero_3:
        print(f'{numero_3} {numero_2} {numero_1}')
    else:
        print(f'{numero_2} {numero_3} {numero_1}')
elif numero_2 >= numero_1 and numero_2 >= numero_3:
    if numero_1 >= numero_3:
        print(f'{numero_3} {numero_1} {numero_2}')
    else:
        print(f'{numero_1} {numero_3} {numero_2}')
elif numero_3 >= numero_1 and numero_3 >= numero_2:
    if numero_1 >= numero_2:
        print(f'{numero_2} {numero_1} {numero_3}')
    else:
        print(f'{numero_1} {numero_2} {numero_3}')
        
    

