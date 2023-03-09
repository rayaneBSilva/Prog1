# Prog1 -UFCG
# Rayane Bezerra da silva
# Imprimindo posição dos elementos.

palavra1= input()
palavra2= input()

for i in range(len(palavra2)):
    posicao = ''
    for j in range(len(palavra1)):
        if palavra2[i] == palavra1[j]:
           posicao += f'{j} '
    if posicao == '':
        print(-1)
    else:
        posicao_elemento= ''
        for e in range(len(posicao) -1):
            if posicao[e] in posicao:
                posicao_elemento += posicao[e]
        print(posicao_elemento)
