# Prog1 - UFCG
# Rayane Bezerra da Silva
# Calculando o quadrante em que determinado numero esta.

grau = int(input())

mensagem = ''

if 0 < grau < 90:
    mensagem = 'Quadrante 1'
elif 90 < grau < 180:
    mensagem = 'Quadrante 2'
elif 180 < grau < 270:
    mensagem = 'Quadrante 3'
elif 270 < grau < 360:
    mensagem = 'Quadrante 4'
elif grau > 360:
    graus = grau - (360 * (grau // 360))
    if 0 < graus < 90:
        mensagem = 'Quadrante 1'
    elif 90 < graus < 180:
        mensagem = 'Quadrante 2'
    elif 180 < graus < 270:
        mensagem = 'Quadrante 3'
    elif 270 < graus < 360:
        mensagem = 'Quadrante 4'
    else:
        mensagem = 'sobre eixos'
else:
    mensagem = 'Sobre eixos'
    
print(mensagem)
