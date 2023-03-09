n = int(input())

antes = 0
entre = 0
depois = 0

numeros = []


for c in range(n):
    numero = int(input())
    numeros.append(numero)
    
print('---')
    
numero1_referencia = int(input())
numero2_referencia = int(input())


for i in range(len(numeros)):
    if int(numeros[i]) <= int( numero1_referencia):
        antes += 1
    elif int(numero1_referencia) <= int(numero[i]) <= int(numero2_referencia):
        entre += 1
    elif int(numero[i]) >= int(numero2_referencia):
        depois += 1
        
print(f'antes {antes}')
print(f'entre {entre}')
print(f'depois {depois}')
