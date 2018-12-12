class NewEmployee:
    num_emps = 0
    raise_amount = 1.04

    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = firstName + '.' + lastName + '@company.com'

        NewEmployee.num_emps += 1

    def fullname(self):
        return '{} {}'.format(self.firstName, self.lastName)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        firstName, lastName, pay = emp_str.split('-')
        return cls(firstName, lastName, pay)


emp_01 = NewEmployee('Carlos', 'Freire', 1500)
print(emp_01)
print(emp_01.raise_amount)

NewEmployee.set_raise_amount(1.05)
print(emp_01.raise_amount)

emp_str_1 = 'Maria-Fonseca-7500'
emp_str_2 = 'Mateus-Silva-3500'
emp_str_3 = 'Janete-Braga-4600'

lista = emp_str_1.split('-')
print(lista)
print(type(lista))

#firstName, lastName, pay = emp_str_1.split('-')
#print('Dados recuperados: {} {} {}'.format(firstName, lastName, pay))

#new_emp_1 = NewEmployee(firstName, lastName, pay)

new_emp_1 = NewEmployee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)
print(new_emp_1.fullname())

new_emp_2 = NewEmployee.from_string(emp_str_2)
print(new_emp_2.fullname())

new_emp_3 = NewEmployee.from_string(emp_str_3)
print(new_emp_3.fullname())
