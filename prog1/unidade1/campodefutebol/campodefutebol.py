#Prog1 -UFCG
#Rayane Bezerra da Silva
#Calculando quantos campo de futebol tem uma determinada área.

area_1 = float(input())
area_2 = float(input())
area_3 = float(input())

campo_de_futebol_1 = (area_1 / 4000)
campo_de_futebol_2 = (area_2 / 4000)
campo_de_futebol_3 = (area_3 / 4000)

media_final = (campo_de_futebol_1 + campo_de_futebol_2 + campo_de_futebol_3) / 3

print(f'{campo_de_futebol_1 :.2f}')
print(f'{campo_de_futebol_2 :.2f}')
print(f'{campo_de_futebol_3 :.2f}')
print(f'{media_final :.2f}')

