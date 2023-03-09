# Prog1 - UFCG
# Rayane Bezerra da silva 
# Calculando letras distintas entre duas palavras.

primeira_palavra = input()
segunda_palavra = input()

distintas = 0 

for letra in range(len(primeira_palavra)):
    ocorrencia = False
    for letra1 in range(len(segunda_palavra)):
        if segunda_palavra[letra1] == primeira_palavra[letra]:
            ocorrencia = True
    if ocorrencia == False:
        distintas += 1

print(distintas)


         
    
    

 
        
