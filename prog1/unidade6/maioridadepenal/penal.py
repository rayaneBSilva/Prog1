# Prog1 -UFCG
# Rayane Bezerra da Silva
# Calcula maioridade penal.


def maioridade_penal(pessoas,idades):
    maioridade = ''
    saida = ''
    pessoa = pessoas.split()
    idade = idades.split()
    
    for i in range(len(pessoa)):
        if int(idade[i]) >= 18:
            maioridade += (pessoa[i])

    return maioridade 

print(maioridade_penal('jasen italo ana' , '14 21 60'))


