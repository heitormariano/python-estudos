num = int(input('Informe um número: '))

if num > 10:
    print('O valor é maior do que 10')
else:
    print('O valor não é maior do que 10')

#É possível usar parentêses entre as condições

prod = input('Informe o produto: ')
valorProd = int(input('Informe o valor do produto: '))

if (valorProd > 100):
    print('O valor {} para o {} é alto'.format(valorProd, prod))
else:
    print('O valor {} para o {} é BOM'.format(valorProd, prod))

