# Prog1 - UFCG
# Rayane Bezerra da Silva
# Calculando a qualidade de um produto.

produto_inicial = float(input())
produto_final = float(input())

porcentagem = ((produto_inicial - produto_final) / produto_inicial) * 100

mensagem1 = ''
mensagem = ''

if porcentagem > 10:
    mensagem1 = f'{porcentagem :.1f}% do peso do produto é de água congelada.'
    mensagem = f'Produto não conforme.'
elif porcentagem < 5:
    mensagem1 = f'{porcentagem :.1f}% do peso do produto é de água congelada.' 
    mensagem = f'Produto qualis A.'
else:
    mensagem1 = f'{porcentagem :.1f}% do peso do produto é de água congelada.'
    mensagem = f'Produto em conformidade.'

print(mensagem1)
print(mensagem)