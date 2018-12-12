class SuperEmployee:
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


class Developer(SuperEmployee):
    raise_amount = 1.10  # aumento de 10% do pagamento

    def __init__(self, firstName, lastName, pay, lang_prog):
        super().__init__(firstName, lastName, pay)
        self.lang_prog = lang_prog


class Manager(SuperEmployee):
    def __init__(self, firstName, lastName, pay, employees=None):
        super().__init__(firstName, lastName, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print('--->', emp.fullname())


# dev_01 = SuperEmployee('Carla', 'Fernandes', 3400.00)
# dev_02 = SuperEmployee('Antonio', 'Faria', 2300.45)

dev_01 = Developer('Carla', 'Fernandes', 3400.00, 'Java')
dev_02 = Developer('Antonio', 'Faria', 2300.45, 'Python')

print(dev_01.firstName)
print(dev_02.firstName)

print(dev_01.pay)
print(dev_02.pay)

# print(help(Developer))

print('Manipulando dados dos objetos')
print('Antes:', dev_01.pay)
dev_01.apply_raise()
print('Depois:', dev_01.pay)

print(dev_01.__dict__)
print(dev_02.__dict__)

print(dev_01.lang_prog)
print(dev_02.lang_prog)

manager_01 = Manager('Heitor', 'Camara', 12900.00, [dev_01])
print('Email:', manager_01.email)
manager_01.print_employees()

print('Printing employees again:')
manager_01.add_employee(dev_02)
manager_01.print_employees()

# uso de métodos: isinstance() e issubclass()
print('Usando isinstance()')
print(isinstance(manager_01, Manager))
print(isinstance(manager_01, SuperEmployee))
print(isinstance(manager_01, Developer))

print(isinstance(dev_01, Developer))
print(isinstance(dev_01, SuperEmployee))
print(isinstance(dev_01, Manager))

print('Usando issubclass()')
print(issubclass(Developer, SuperEmployee))
print(issubclass(Manager, SuperEmployee))
print(issubclass(Developer, Manager))
