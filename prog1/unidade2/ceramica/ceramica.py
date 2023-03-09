#Prog1 -UFCG
#Rayane Bezerra da Silva 
#Calcular quantas caixas de cerâmicas um construtor precisará para cobrir determinada área 

revestimento = float(input( 'Capacidade de revestimento? \n'))

print( '== Dados do vão a revestir ==')

comprimento = float(input( 'Comprimento? '))
largura = float(input( 'Largura? '))
altura = float(input( 'Altura? \n'))

print('== Resultados ==')

area = (comprimento * largura) + 2 * (largura * altura) + 2 * (comprimento * altura)
ceramica = area/revestimento

print(f'Área total a revestir: {area} m2')
print(f'Número de caixas: {ceramica :.0f}')