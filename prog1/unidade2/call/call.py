# Prog1 -UFCG
# Rayane Bezerra da Silva
# Calculando media de atendimentos.

segunda = int(input())
terça =  int(input())
quarta = int(input())
quinta = int(input())
sexta = int(input())
sabado = int(input())
domingo = int(input())

soma = segunda + terça + quarta + quinta + sexta + sabado + domingo
media = soma / 7

print(f'Total: {soma}')
print(f'Média: {media :.2f}')
