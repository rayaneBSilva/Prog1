# Prog1 -UFCG
# Rayane Bezerra da Silva
# Analisando créditos e notas de um aluno, para participar do Ciências sem Fronteira.

nota_enem = int(input())
creditos = int(input())

minimo = (416 * 20) / 100
maximo = (416 * 90) / 100
mensagem = ''

if nota_enem < 600 and creditos >= minimo and creditos <= maximo:
    mensagem = 'Condição ENEM não satisfeita.'
elif nota_enem >= 600 and (creditos < minimo or creditos > maximo):
    mensagem = 'Condição CRÉDITOS não satisfeita.'
elif nota_enem >= 600 and creditos >= minimo and creditos <= maximo:
    mensagem = 'Todas as condições satisfeitas.'
else:
    mensagem = 'Nenhuma condição satisfeita.'

print(mensagem)
