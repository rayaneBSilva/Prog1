# Prog1 -UFCG
# Rayane Bezerra da Silva
# Calculando a quantidade de morangos em uma caixa 

morangos = int(input())
caixas_completas = morangos // 400
resto = morangos % 400
sobras = (resto * 100) / morangos
print(f'{caixas_completas} caixa(s) completa(s) para embalar os morangos.')
print(f'{sobras :.1f}% dos morangos serão perdidos.')

