# Prog1 - UFCG
# Rayane Bezerra da Silva
# Codificando uma palavra.

palavra = input()
palavra_codificada = palavra[0]
contador = 0

for i in range(1, len(palavra)):
    if palavra[i] == 'a' or palavra[i] == 'A':
        palavra_codificada += '4'
        contador += 1
    elif palavra[i] == 'e' or palavra[i] == 'E':
        contador += 1
        palavra_codificada += '3'
    elif palavra[i] == 'i' or palavra[i] == 'I':
        palavra_codificada += '1'
        contador += 1
    elif palavra[i] == 'o' or palavra[i] == 'O':
        palavra_codificada += '0'
        contador += 1
    else:
        palavra_codificada += palavra[i]
    
print(f'{palavra_codificada} ({contador} troca(s))')

