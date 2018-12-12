# loop while

count = 0
while count < 10:
    print(count)
    count += 1  # equilave a count = count + 1
print('Good Bye!')

count = 0
while count < 10:
    if count % 2 == 0:
        print(count, ' - Numero Par')
    else:
        print(count, '- Numero Impar')
    count += 1
print('Good Bye again')

# continue
for letter in 'Python':
    if letter == 'h':
        continue
    print('Current Letter :', letter)

# infinite while example
#count = 1

# while count == 1:
#    num = int(input('Informe um numero:'))
#    print('Voce informou:', num)

#print('Good Bye!')

for n in range(10):
    if n == 5:
        break
    else:
        print('Valor de n:', n)

word = 'IFRN'

for letter in word:
    if letter == 'R':
        break
    else:
        print('Letra:', letter)
