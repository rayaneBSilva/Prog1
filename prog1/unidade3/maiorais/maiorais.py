# Prog1 - UFCG
# Rayane Bezerra da Silva
# Determinando o time vencedor.

gols_campinense = int(input())
gols_treze = int(input())

mensagem = ''

if gols_campinense > gols_treze:
    mensagem = 'Campinense'
elif gols_treze > gols_campinense:
    mensagem = 'Treze'
else:
    mensagem = 'Empate'

print(mensagem)