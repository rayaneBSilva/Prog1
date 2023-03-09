frase = 'um coração gelado'
palavra = ''
frases = []

for i in range(len(frase)):
    palavra += frase[i]
    if frase[i] == ' ':
        palavra += ', '
        
    
print(palavra)



