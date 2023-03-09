# Prog1 -UFCG
# Rayane Bezerra da Silva
# Calculando a receita de uma empresa.

meses = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
lucros = []

for c in range(12):
   valores = input().split()
   receitas = float(valores[0])
   despensa = float(valores[1])
   lucro = receitas - despensa
   lucros.append(lucro)
   
for i in range(len(lucros)):
   print(f'{meses[i]} {lucros[i]:4.1f}')
