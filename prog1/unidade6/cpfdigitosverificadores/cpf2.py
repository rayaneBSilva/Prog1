# Prog1 -UFCG
# Rayane Bezerra da Silva
# Encontrando digitos verificadores de cpf.

def calcula_digitos_verificacao(cpf):
    cont_1 = 2
    cont_2 = 3
    soma_digito1 = 0
    soma = 0
    soma_digito_2 = 0
    saida = ''
    
    for i in range(len(cpf)-1, -1,-1):
        soma_digito1 += int(cpf[i]) * cont_1
        cont_1 += 1
        primeiro_digito = (10 * soma_digito1) % 11
    
        if primeiro_digito == 10:
            primeiro_digito = 0
    
        digito9 = primeiro_digito * 2
        soma +=  int(cpf[i]) * cont_2
        soma_digito_2 = soma + digito9
        cont_2 += 1
        segundo_digito = (10 * soma_digito_2) % 11 
    
        if segundo_digito == 10:
            segundo_digito = 0
        
        saida = str(primeiro_digito) + str(segundo_digito)
        
    return saida



