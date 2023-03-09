# Prog1 -UFCG
# Rayane Bezerra da Silva
# Informando o valor da contribuição.

area_construida = float(input())
metro_quadrado = float(input())
forma_de_pagamento = input()

mensagem = ''

if forma_de_pagamento == 'vista':
    total = area_construida - ((area_construida * metro_quadrado) * 0.20)
    mensagem = f'Total: R$ {total :.2f}'
elif forma_de_pagamento == '2x':
    total = area_construida - ((area_construida * metro_quadrado) * 0.10)
    parcelas = total / 2
    mensagem = f'Total: R$ {total :.2f}. Parcelas: R$ {parcelas :.2f}'
elif forma_de_pagamento == '3x':
    total = area_construida - ((area_construida * metro_quadrado) * 0.05)
    parcelas = total / 3
    mensagem = f'Total: R$ {total :.2f}. Parcelas: R$ {parcelas :.2f}'

print(mensagem)
