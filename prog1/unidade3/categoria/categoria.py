# Prog1 - UFCG
# Rayane Bezerra da Silva
# Determinar a categoria de um nadador, por meio de sua idade.

nome = input()
idade = int(input())
mensagem = ''

if idade >= 5 and idade <= 7:
    mensagem = f'{nome}, {idade} anos, Infantil A.'
elif idade > 7 and idade <= 10:
    mensagem = f'{nome}, {idade} anos, Infantil B.'
elif idade > 10 and idade <= 13:
    mensagem = f'{nome}, {idade} anos, Juvenil A.'
elif idade >= 14 and idade <= 17:
    mensagem = f'{nome}, {idade} anos, Juvenil B'
elif idade > 17:
    mensagem = f'{nome}, {idade} anos, Senior.'
else:
    mensagem = f'{nome}, {idade} anos, Não pode competir.'

print(mensagem)
