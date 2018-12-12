import pickle
str_01 = 'IFRN'
x = pickle.dumps(str_01)  # método dumps serializa a string
print(x)

# testes
print(type(x))  # a variável x contém bytes
retorno_str = pickle.loads(x)
print(retorno_str)
print(type(retorno_str))
