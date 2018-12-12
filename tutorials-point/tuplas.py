# Tuplas

# Diferença básica entre listas e tuplas
# Listas - elementos da lista ficam entre "[]" e podem ser atualizado
# Tuplas - elementos da lista ficam entre "()" e NÂO podem ser atualizados

tupla = ('Massa', 1, 'Show', 2, 'Perfeito', 458.2)
lista = ['Legal', 10, 'Bacana', 50, 'Uhuuu', 12.6]

# tupla[0] = 'Supimpa' # operação inválida
lista[0] = 'Supimpa'  # operação permitida

print("Tupla:" + str(tupla))
