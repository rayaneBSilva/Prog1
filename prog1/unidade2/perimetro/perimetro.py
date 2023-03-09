import math

x1 = int(input())
x2 = int(input())
x3 = int(input())
y1 = int(input())
y2 = int(input())
y3 = int(input())

dij = ((x1 - x2 - x3) ** 2) + ((y1 - y2 - y3) ** 2)
raiz = math.sqrt(dij)

print(raiz)