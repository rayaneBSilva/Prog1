# Prog1 - UFCG
# Rayane Bezerra da Silva
# Verificando se um determinado ano é bissexto.

ano = int(input())

if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    mensagem = f'{ano} é bissexto'
else:
    mensagem = f'{ano} não é bissexto'

print(mensagem)