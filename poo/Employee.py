class Employee:
    num_emps = 0
    raise_amount = 1.04

    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = firstName + '.' + lastName + '@company.com'

        Employee.num_emps += 1

    def fullname(self):
        return '{} {}'.format(self.firstName, self.lastName)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


# criando objetos
emp_01 = Employee('Fernando', 'Almeida', 2000)
emp_02 = Employee('Gessica', 'Silva', 4000)

print(emp_01)
print(emp_02)

print(emp_01.email)
print(emp_02.email)

print(emp_01.fullname())
print(emp_02.fullname())

print('Another Way: ' + Employee.fullname(emp_01))
print('Another Way: ' + Employee.fullname(emp_02))

# atributo da instância X atributo da classe

print(emp_01.raise_amount)

emp_01.raise_amount = 1.05  # novo valor de aumento para o salário
print(emp_01.raise_amount)

emp_01.apply_raise()  # novo valor de aumento é visto apenas na instância emp_01
print(emp_01.pay)  # 2100

# valor de aumento não é alterado para a instância emp_02
print(emp_02.raise_amount)
emp_02.apply_raise()
print(emp_02.pay)

# Mudando valor de aumento para a classe Employee
Employee.raise_amount = 1.06
print(Employee.raise_amount)

print(emp_01.raise_amount)  # valor de aumento não sofreu mudança
emp_01.apply_raise()  # 2205
print(emp_01.pay)


# valor de aumento foi alterado. Assumiu o novo valor definido para a classe
print(emp_02.raise_amount)

# uso do método __dict__
# Interessante observar as informações encontradas para as instâncias(emp_01 e emp_02) e para a classe Employee
print(emp_01.__dict__)
print(emp_02.__dict__)
print(Employee.__dict__)

# Conferir o número de empregados
print(Employee.num_emps)
