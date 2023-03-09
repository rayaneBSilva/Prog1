# Prog1 -UFCG
# Rayane Bezerra da silva
# Encontrando menor elemento, apartir de um dado numero base.

def encontra_menores(num,lista):
    for numeros in lista:
        if int(numeros) < num:
            return numeros
        
    return -1

