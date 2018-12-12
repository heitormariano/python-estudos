# listas

lista1 = [2, 3, 4, 5, 6, 7, 8]
# índice final é 5, mas no slice (recorte) será considerado até 4 (ind.final - 1)
print(lista1[:5])

lista2 = [3 * x for x in lista1]
print(lista2)
# lista2[6,9,12,15,18,21,24]

# slice ---> Recorte. Lista[ind_inicial:indice_final:passo]

# Cenário: indice inicial igual a 0. índice final não definido. Passo com valor 3
# O valor do índice 0 mudará para 3, 6 até o último índice possivel
print(lista2[0::3])

print(lista1[3::-1])
print(lista1[2:6:2])
