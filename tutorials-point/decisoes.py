print('Revendo tomadas de decisoes em Python')

num = 250

if num % 2 == 0:
    print('Numero é par')
else:
    print('Numero é par')


num_02 = 233

if num_02 == 233:
    print('Valor igual a 233')

#single statement suites
num_03 = 450
if num_03 == 450: print('Valor igual a 450')
print('Fim')


valor = 100

if valor % 2 == 0:
    if valor % 3 == 0:
        print('Valor divisivel por 2 e também por 3')
    else:
        print('Valor divisivel apenas por 2')
else:
    if valor % 3 == 0:
        print('Valor divisivel por 3')
    else:
        print('Valor nao e divisivel por 2 e nem por 3')