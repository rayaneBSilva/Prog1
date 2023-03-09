# Prog1 - UFCG
# Rayane Bezerra da Silva
# Calculando o preço do serviço de limpeza.

codigo_indicativo = input()

mensagem = ''

if codigo_indicativo == '1':
    metros_cubicos = float(input())
    total = metros_cubicos * 80.00
    print(f'R$ {total :.2f}')
    if total >= 200.00:
        print('Brinde!')
elif codigo_indicativo == '2':
    metros_cubicos = float(input())
    total = metros_cubicos * 50.00
    print(f'R$ {total :.2f}')
    if total >= 200.00:
        print('Brinde!')
else:
    print('R$ 50.00')
