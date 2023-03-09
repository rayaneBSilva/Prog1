# Prog1 - UFCG
# Rayane Bezerra da Silva
# Verificando se um elemento esta em uma lista.

inteiro = input()
sequencia = input().split()

for numero in sequencia:
    if inteiro == numero:
        print('sim')
        break
    
if inteiro != numero:
    print('não')
