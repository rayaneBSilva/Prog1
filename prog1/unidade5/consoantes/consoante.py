# Prog1 -UFCG
# Rayane Bezerra da Silva
# Calculando mais consoantes em uma palavra.

def minhas_vogais(palavras):
    vogais = 0
    consoantes = 0
    for letra in palavras:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            vogais += 1
        elif letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
            vogais += 1
        else:
            consoantes += 1
    if consoantes > vogais:
        return True
    else:
        return False
   

contador = 0

while True:
    palavra = input()
    contador += 1
    if minhas_vogais(palavra) == True: break 
    
    
print(contador)