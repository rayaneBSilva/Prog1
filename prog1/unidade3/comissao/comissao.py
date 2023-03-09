# Prog1 - UFCG
# Rayane Bezerra da Silva
# Calculando a comissao de um vendedor.

vendedor = input('Qual é o nome do(a) vendedor(a)? ')
venda = float(input('Qual é o valor da venda? '))

mensagem = ''

if venda <= 500.00:
    comissao = (venda * 0.05)
    mensagem = f'O valor da comissão para o(a) vendedor(a) {vendedor} é R$ {comissao :.2f}.'
else:
    comissao = (venda * 0.10)
    mensagem = f'O valor da comissão para o(a) vendedor(a) {vendedor[0:5]} é R$ {comissao :.2f}.' 
 
print(mensagem)   