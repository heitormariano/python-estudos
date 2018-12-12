print('Questão concurso')
s = tuple(range(-8, 8, 3))
y = 1

# Interpretador não reconhece o operador ++
# Contudo, o código executa normalmente
for x in s:
    if ++x > 2:
        continue
    y += abs(x)

print(y)

# testando o método range(stop)
print('Testando uso do método range(stop)')
for i in list(range(6)):
    print(i)

# testando o método range(start, stop)
print('Testando uso do método range(start, stop)')
for j in list(range(4, 8)):
    print(j)

# testando o método range(start, stop, step)
print('Testando uso do método range(start, stop, step)')
for k in list(range(0, 10, 2)):
    print(k)

# Criando um código parecido com o da questão do concurso
print('Novo código com impressão')
tupla_teste = tuple(range(-10, 10, 2))
num = 1

for elem in tupla_teste:
    elem += 1
    if elem > 2:
        continue
    num += abs(elem)

print(num)
