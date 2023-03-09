# Prog1 -UFCG
# Rayane Bezerra da silva
# Calculando quantos alunos foram reprovados.

reprovados = 0

while True:
    alunos = input('')
    if alunos == '-': break
    faltas = 0
    i = 0
    while i < len(alunos):
        if alunos[i] == 'f':
            faltas += 1
        i += 1
    if faltas > 8:
        reprovados += 1
       
print(f'{reprovados} aluno(s) reprovado(s) por falta.')
        

    
