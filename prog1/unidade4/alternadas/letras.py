palavra = input()

nao_invertida = []
invertida = []
contador = 0

for letra in palavra:
    nao_invertida.append(letra)
    
for i in range(len(palavra) -1,-1,-1):
    invertida.append(palavra[i])
    
for i in range(len(nao_invertida)):
    if nao_invertida[i] == invertida[i]:
        contador += 1
        
print(f'a palavra {palavra} contêm {contador} caractere(s) coincidente(s) com sua inversa')
    