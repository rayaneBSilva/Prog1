def analisando_sequencia(numeros):
    i = 0
    status = False
    while i < len(numeros):
        if numeros[i] == 'a' and numeros[i + 1] == 'i' or numeros[i + 1] == 'c':
            status = True
    return status

            
sequencia = input()
print(analisando_sequencia(sequencia))
