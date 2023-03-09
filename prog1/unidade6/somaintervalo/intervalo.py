# Prog1 -UFCG
# Rayane Bezerra da Silva
# Criando funçao que soma um intervalo.


def soma_intervalo(a,b):
    soma = 0
    for c in range(a,b + 1):
        soma += c
    return soma
    

def s_intervalo(a, b):
    num = 0
    for i in range(a,b + 1):
        num += i
    return num
    
print(soma_intervalo(10,10))
print(s_intervalo(10,10))
    