# Prog1 -UFCG
# Rayane Bezerra da silva
# Calculando números acima da media.

media = float(input())

maiormedia = 0
maiorsequencia = []

while True:
    dados = input().split()
    if dados[0] == "fim": break
    
    soma = 0
    for dado in dados:
        soma += int(dado)

    mediadados = soma / len(dados)
    if mediadados < media / 2:
        break
    
    if mediadados > maiormedia:
        maiormedia = mediadados
        maiorsequencia = dados

saida = ""

for i in range(len(maiorsequencia)):
    if i < len(maiorsequencia) - 1:
        saida += f"{maiorsequencia[i]} "
    else:
        saida += maiorsequencia[i]

print(saida)
    
    
