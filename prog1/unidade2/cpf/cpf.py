# Prog1 -UFCG
# Rayane Bezerra da silva
# Formatando cpf e calculando a soma dos ultimos dois digitos.

cpf1 = int(input())
cpf2 = int(input())
cpf3 = int(input())

cpf_1 = cpf1 // 100
cpf_2 = cpf2 // 100
cpf_3 = cpf3 // 100

penultimo_digito_cpf1 = ( cpf1 // 10 ) % 10
penultimo_digito_cpf2 = ( cpf2 // 10 ) % 10
penultimo_digito_cpf3 = ( cpf3 // 10 ) % 10

ultimo_digito_cpf1 = ( cpf1 // 1 ) % 10
ultimo_digito_cpf2 = ( cpf2 // 1 ) % 10
ultimo_digito_cpf3 = ( cpf3 // 1 ) % 10

soma_cpf1 = penultimo_digito_cpf1 + ultimo_digito_cpf1
soma_cpf2 = penultimo_digito_cpf2 + ultimo_digito_cpf2
soma_cpf3 = penultimo_digito_cpf3 + ultimo_digito_cpf3

print(f'{cpf_1}-{penultimo_digito_cpf1}{ultimo_digito_cpf1}')
print(soma_cpf1)
print(f'{cpf_2}-{penultimo_digito_cpf2}{ultimo_digito_cpf2}')
print(soma_cpf2)
print(f'{cpf_3}-{penultimo_digito_cpf3}{ultimo_digito_cpf3}')
print(soma_cpf3)
