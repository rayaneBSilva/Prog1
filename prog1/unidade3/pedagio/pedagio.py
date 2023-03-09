# Prog1 -UFCG
# Rayane Bezerra da Silva
# Calculando o preço do pedagio.

tipo_veiculo= input()

mensagem = ''

if tipo_veiculo == 'Automóvel utilitário':
    mensagem = 'Valor a pagar: R$ 11.40.'
elif tipo_veiculo == 'Motocicleta':
    mensagem = 'Valor a pagar: R$ 5.70.'
elif tipo_veiculo == 'Ônibus':
    eixo = int(input())
    pedagio = eixo * 11.40
    mensagem = f'Valor a pagar: R$ {pedagio :.2f}.'
elif tipo_veiculo == 'Caminhão':
    eixo = int(input())
    pedagio = eixo * 9.60
    mensagem = f'Valor a pagar: R$ {pedagio :.2f}.'
else:
    mensagem = 'Veículo não cadastrado.'

print(mensagem)
