# Prog1 - UFCG
# Rayane Bezerra da Silva
# Calculando o IPTU.

area_construida = float(input('Área construída? '))
aliquota = float(input('Alíquota? '))
iptu = (area_construida * aliquota) + 35.00

print(f'IPTU: R$ {iptu :.2f}\n')

print('Pagamento:')

quota_unica = iptu - (iptu * 0.25)
seisvezes = iptu -( iptu * 0.05)
dezvezes = iptu / 10

print(f'1. Quota única. R$ {quota_unica :.2f}')
print(f'2. Em 6 parcelas. Total: R$ {seisvezes :.2f}')
print(f'   6 x R$ {seisvezes/6 :.2f}')
print(f'3. Em 10 parcelas. Total: R$ {iptu :.2f}')
print(f'   10 x R$ {dezvezes:.2f}')


