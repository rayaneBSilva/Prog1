# Prog1 -UFCG
# Rayane Bezerra da Silva.
# Analisando equipes.

jogadores = []
mensagem = ''

while True:
    jogador = input()
    if jogador != "-":
        jogadores.append(jogador)
        quantidade = len(jogadores)
    if jogador == "-" :
        break

if quantidade == 11:
    mensagem = f"Modalidade -> Futebol"
elif quantidade == 5:
    mensagem = f"Modalidade -> Basquete"
elif quantidade == 6:
    mensagem = f"Modalidade -> Vôlei"
elif quantidade == 7:
    mensagem = f"Modalidade -> Handebol"
else:
    mensagem = f"Equipe Inválida"
    
print(mensagem)