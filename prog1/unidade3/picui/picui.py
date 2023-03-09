atual_recorde = float(input())
quantidade_carne = float(input())

mensagem = ''

if atual_recorde > quantidade_carne:
    mensagem = 'recorde mantido'
elif atual_recorde < quantidade_carne:
    mensagem = f'recorde quebrado ({quantidade_carne} kg)'
else:
    mensagem = 'recorde empatado'
    
print(mensagem)
