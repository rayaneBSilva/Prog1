# Prog1 -UFCG
# Rayane Bezerra da Silva
# analisando posiçoes.

entrada = input().split()

coluna = int(entrada[0])
linha = int(entrada[1])
soma = 0

while True:
    sequencia = input().split()
    if sequencia[0] == "X": break

    direçao = sequencia[0]
    passos = int(sequencia[1])
    soma += passos
    
    if direçao == "C":
        linha = linha - passos
    if direçao == "B":
        linha = linha + passos 
    if direçao == "D":
        coluna = coluna + passos
    if direçao == 'E':
        coluna = coluna - passos
    
    
    print(f"> {linha} {coluna}")

print(soma)
        
        
    
    
    
    
    
        
