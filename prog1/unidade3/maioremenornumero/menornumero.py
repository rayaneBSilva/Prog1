# Prog1 -UFCG
# Rayane Bezerra da silva
# Calculando segundo maior e segundo menor.

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a >= b and a >= c and a >=d:
    maior= a
    if b >= c and b >= d:
        segundo_maior= b
    elif c >= b and c >=d:
        segundo_maior= c
    else:
        segundo_maior= d
elif b >= a and b >= c and b >= d:
    maior= b
    if a >= c and a >= d:
        segundo_maior= a
    elif c >= a and c >= d:
        segundo_maior= c
    else:
        segundo_maior= d
elif c >= a and c >= b and c >= d:
    maior= c
    if a >= b and a >= d:
        segundo_maior= a
    elif b >= a and b >=d:
        segundo_maior= b
    else:
        segundo_maior= d
elif d >= a and d >= c and d >= b:
    maior= d
    if a >= c and a >= b:
        segundo_maior= a
    elif c >= a and c >= b:
        segundo_maior= c
    else:
        segundo_maior= b
if a <= b and a <= c and a <= d:
    menor= a
    if b <= c and b <= d:
        segundo_menor= b
    elif c <= a and c <=d:
        segundo_menor= c
    else:
        segundo_menor= d
elif b <= c and b <= a and b <= d:
    menor= b
    if a <= c and a <= d:
        segundo_menor= a
    elif c <= a and c <= d:
        segundo_menor= c
    else:
        segundo_menor= d
elif c <= b and c <= a and c <= d:
    menor= c
    if b <= a and b <= d:
        segundo_menor= b
    elif a <= b and a <= d:
        segundo_menor= a
    else:
        segundo_menor= d
elif d <= b and d <= c and d <= a:
    menor= d
    if b <= c and b <= a:
        segundo_menor= b
    elif c <= b and c <= a:
        segundo_menor= c
    else:
        segundo_menor= a
        
print(f'Considerando os números {a}, {b}, {c} e {d}')
print(f'O segundo menor número é {segundo_menor}')
print(f'O segundo maior número é {segundo_maior}')

