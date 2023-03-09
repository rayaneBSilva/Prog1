# Prog1 - UFCG
# Rayane Bezerra da Silva
# Verificando se um triângulo é válido ou inválido.

a = int(input())
b = int(input())
c = int(input())

soma_dos_lados = a + b + c 
mensagem = ''

if b - c < a < + b + c:
    mensagem = f'triangulo valido. {soma_dos_lados}'
else:
    mensagem = 'triangulo invalido.'
    
print(mensagem)