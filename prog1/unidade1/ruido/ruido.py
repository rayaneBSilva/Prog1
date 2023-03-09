# Prog1 - UFCG
# Rayane Bezerra da Silva
# Matricula 120210483.
# Analisando se houve ou não ruido, fora do horario permitido.

ruido = input()
horas = int(input())

mensagem = ''

if ruido != '':
    mensagem = 'Condomínio em Paz.'
    if horas >= 22 and horas <= 24 or horas <= 6:
        mensagem = f'Perturbação Detectada!'
else:
    mensagem = f'Condomínio em Paz.'

print(mensagem)