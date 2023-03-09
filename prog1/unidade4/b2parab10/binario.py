# Prog1 -UFCG
# Rayane Bezerra da Silva
# Trasnformando base binaria em hexadecimal.

binario = input()

cont = 0
soma = 0

for i in range(len(binario)):
    cont -= 1
    potencia = 2 ** int(len(binario) + cont)
    resultado = int(binario[i]) * int(potencia)
    soma += int(resultado)
    print(f'{binario[i]} * {potencia} = {resultado}')
    
print(f'{binario}(2) = {soma}(10)')
    

