# Prog1 -UFCG
# Rayane Bezerra da Silva
# Transformando programa de tabuada de for para while.

fator = int(input())

i = 0

while i < 11:
    produto = i * fator
    print(f"{fator}  x {i:2}  = {produto:3}")
    i += 1
    