def colapsa_n_menores(n,lista):
     soma = 0
     for i in range(len(lista) - 1):
        for j in range(len(lista) - 1):
            if int(lista[j]) < int(lista[j + 1]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
     
     for c in range(n):
          soma += lista[c]
          
          
     lista.append(soma)
     return lista

lista1 = [12,3,7,1,5,10]
print(colapsa_n_menores(3,lista1))

