senha = input()

for i in range(len(senha)-1):
    if int(senha[i]) % 2 == 0 and int(senha[i + 1]) % 2 == 0:
        mensagem = 'senha insegura'
    elif int(senha[i]) % 2 != 0 and int(senha[i + 1]) % 2 != 0:
        mensagem = 'senha insegura'
    elif int(senha[i]) % 2 == 0 and int(senha[i + 1]) % 2 != 0:
        mensagem = 'senha segura'
    elif int(senha[i]) % 2 != 0 and int(senha[i + 1]) % 2 == 0:
        mensagem = 'senha segura'
    else:
        mensagem = 'senha insegura'
    
print(mensagem)