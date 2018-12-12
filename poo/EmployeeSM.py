class EmployeeSM:
    raise_amount = 1.04

    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = firstName + '.' + lastName + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.firstName, self.lastName)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # special methods
    def __repr__(self):
        return "EmployeeSM('{}', '{}', {})".format(self.firstName, self.lastName, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_01 = EmployeeSM('Heitor', 'Camara', 4560.50)
print(emp_01)  # o método __repr__() é usado
print(emp_01.fullname())

print(emp_01.__repr__())
print(repr(emp_01))

print(emp_01.__str__())
print(str(emp_01))

emp_02 = EmployeeSM('Jedi', 'Silva', 5640.60)
print('Somando salários: ', emp_01 + emp_02)

print('Tamanho String: ' + str(len('teste')))
print('Testando tamanho da String de novo:', 'teste'.__len__())

print('Emp_01 - uso __len__():', emp_01.__len__())
print(len(emp_01))

print('Emp_02 - uso __len__():', emp_02.__len__())
print(len(emp_02))
