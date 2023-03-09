# Prog1 - UFCG
# Rayane Bezerra da Silva
# Calculando o quadrante em que determinado numero esta.

angulo = int(input())

if angulo == 0 or angulo == 90 or angulo == 180 or angulo == 270 or angulo == 360:
    mensagem = 'Sobre eixos'
elif angulo > 0 and angulo < 90:
    mensagem = 'Quadrante 1'
elif angulo > 90 and angulo < 180:
    mensagem = 'Quadrante 2'
elif angulo > 180 and angulo < 270:
    mensagem = 'Quadrante 3'
elif angulo > 270 and angulo < 360:
    mensagem = 'Quadrante 4'
else:
    posiçao_final = angulo - ((angulo // 360) * 360)
    if posiçao_final > 0 and posiçao_final < 90:
        mensagem = 'Quadrante 1'
    elif posiçao_final > 90 and posiçao_final < 180:
        mensagem = 'Quadrante 2'
    elif posiçao_final > 180 and posiçao_final < 270:
        mensagem = 'Quadrante 3'
    elif posiçao_final > 270 and posiçao_final < 360:
        mensagem = 'Quadrante 4'
    else:
        mensagem = 'Sobre eixos'

print(mensagem)

