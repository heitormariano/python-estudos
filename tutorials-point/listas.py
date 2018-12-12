#usando listas

listaVariada = ['Joao', 123, 'Carlos', 55.26]

listaPequena = ['Andre', 260]

print(listaVariada)
print(listaVariada[2])
print(listaVariada[0:3])
print(listaVariada[:1])
print(listaVariada[2:])

print(listaPequena)
print(listaPequena[0])
print(listaPequena * 2)
print(listaPequena * 3)

print('As duas listas concatenadas')
print(listaVariada + listaPequena)

print('Elementos lista variada')
for item in listaVariada :
    print(item)

print('Elementos lista pequena')
for item in listaPequena :
    print(item)

print('substituindo alguns valores de listaVariada')

print('Lista antes: ' + str(listaVariada))

listaVariada[0] = 'Supimpa'
listaVariada[3] = 300

print('lista depois: ' + str(listaVariada))
# print('Elemento:' + str(listaVariada[-1]))