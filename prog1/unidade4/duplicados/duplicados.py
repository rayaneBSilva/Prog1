# Prog1 - UFCG
# Rayane Bezerra da Silva
# Encontrando duplicados.

numero_1 = int(input())
numero_2 = int(input())
numero_3 = int(input())
numero_4 = int(input())
numero_5 = int(input())

mensagem = ''

if numero_1 == numero_2 or numero_1 == numero_3 or numero_1 == numero_4 or numero_1 == numero_5:
    mensagem = 'com duplicados'
elif numero_2 == numero_3 or numero_2 == numero_4 or numero_2 == numero_5:
    mensagem = 'com duplicados'
elif numero_3 == numero_4 or numero_3 == numero_5:
    mensagem = 'com duplicados'
elif numero_4 == numero_5:
    mensagem = 'com duplicados'
else:
    mensagem = 'sem duplicados'
    
print(mensagem)