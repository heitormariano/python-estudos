
lista01 = [1, 2, 3, 4, 5]
lista02 = [3 * x for x in lista01]

print("Imprimindo as listas")
print(lista01)
print(lista02)

print("Slices com a lista01")
print(lista01[1:3])
print(lista01[3:])
print(lista01[:4])

print("Slices com a lista02")
print(lista02[0:3])
print(lista02[1::2])
print(lista02[:1])
print(lista02[2::-1]) #com o passo negativo (-1), os elementos são recuperados na ordem inversa


class Equipamento:
    def __init__(self, cod):
        self.cod = cod

class Impressora(Equipamento):
    def __init__(self, cod, marca, sala):
        super().__init__(cod)
        self.marca = marca
        self.sala = sala

equip = Equipamento(1)
print('Código Equipamento:', equip.cod)

impress = Impressora(1, 'HP', 'Lab.Redes')
print('Marca Impressora:', impress.marca)
print('Sala Impressora:', impress.sala)

print('Usando o módulo pickle')
import pickle

str_01 = 'IFRN'
retorno_str = pickle.dumps(str_01)
print(type(retorno_str))

result_str = pickle.loads(retorno_str)
print(result_str)
print(type(result_str))

print('Usando o range')
lista = list(range(0,10))
for elem in lista:
    print(elem)
print('Imprimindo elementos de nova lista')
lista02 = list(range(2,12,2))
for elem in lista02:
    print(elem)
