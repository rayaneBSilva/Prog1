# Prog1 - UFCG
# Rayane Bezerra da silva

sequencia = input()

inteiro = []
mensagem = ''

for inteiros in sequencia:
    inteiro.append(int(inteiros))
    
for i in range(len(inteiro)-1):
    if inteiro[i] % 2 == 0 and inteiro[i + 1] % 2 != 0:
        mensagem = f'verdadeiro: {len(inteiro)} algarismos.'
    elif inteiro[i] % 2 != 0 and inteiro[i + 1] % 2 == 0:
        mensagem = f'verdadeiro: {len(inteiro)} algarismos.'
    elif inteiro[i] % 2 == 0 and inteiro[i + 1]:
        mensagem = f'falso: {len(inteiro)} algarismos.'
        break
print(mensagem)
    
