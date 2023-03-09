# Prog1 - UFCG
# Rayane Bezerra da Silva
# Calculando a capacidade máxima de um elevador.

capacidade_do_elevador = int(input())
peso_medio = int(input())
capacidade_maxima = capacidade_do_elevador // peso_medio

print(f'O elevador pode transportar {capacidade_maxima} pessoas com segurança.')