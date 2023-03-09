# Prog1 -UFCG
# Rayane Bezerra da Silva
# Analisando prioridade da vacina.

infratores = 0
cont_postos = 0

while True:
    entrada = input()
    if entrada == "###": break
    cont_postos += 1
    i = 0
    while i < len(entrada) - 1:
        if entrada[i] == "a" and entrada[i + 1] != "a":
            infratores += 1
            break
        i += 1

print(f"sim: {cont_postos - infratores}")
print(f"não: {infratores}")
