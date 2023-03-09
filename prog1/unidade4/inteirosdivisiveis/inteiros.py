# Prog1 -UFCG
# Rayane Bezerra da Silva
# imprimindo numeros divisiveis por a e b ao mesmo tempo.

A = int(input())
B = int(input())
K = int(input())

for i in range(1,K + 1):
    if i % A == 0 and i % B == 0:
        if i <= K:
            print(i)