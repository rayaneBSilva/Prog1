# Prog1 -UFCG
# Rayane Bezerra da Silva
# Encontrando afinidade musical.

def tem_afinidade(l1,l2):
    afinidade = 0
    
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                afinidade += 1
    if afinidade >= 3:
        return True
    
    return False

