# Prog1 - UFCG
# Rayane Bezerra da Silva
# Encontrando letras coicidentes em uma palavra inversa.

palavra = input()

letras = []
invertidas = []
coincidentes = 0

for i in range(len(palavra) -1, -1, -1):
    invertidas.append(palavra[i])
    
for i in range(len(invertidas)):
    if invertidas[i] == palavra[i]:
        coincidentes += 1
        
print(f'A palavra {palavra} contém {coincidentes} caractere(s) coincidente(s) com a sua inversa.')
