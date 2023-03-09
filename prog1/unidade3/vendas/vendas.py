# Prog1 - UFCG
# Rayane Bezerra da Silva
# Calculando a porcentagem de vendas de cada vendedor.

brinquedos_vendidos = int(input())
brinquedos_teresa = int(input())
brinquedos_carla = int(input())

brinquedos_joao = brinquedos_vendidos - (brinquedos_carla + brinquedos_teresa)

porcentagem_teresa = ( brinquedos_teresa / brinquedos_vendidos ) * 100
porcentagem_carla = ( brinquedos_carla / brinquedos_vendidos ) * 100
porcentagem_joao = ( brinquedos_joao / brinquedos_vendidos ) * 100

print(f'Teresa vendeu {brinquedos_teresa} (de {brinquedos_vendidos}) brinquedos. ({porcentagem_teresa :.2f}%)')
print(f'Joaquim vendeu {brinquedos_joao} (de {brinquedos_vendidos}) brinquedos. ({porcentagem_joao :.2f} %)')  
print(f'Carla vendeu {brinquedos_carla} (de {brinquedos_vendidos} brinquedos. ({porcentagem_carla :.2f})%)')
