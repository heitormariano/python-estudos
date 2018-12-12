class EmployeePD:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        #self.email = firstName + '.' + lastName + '@company.com'

    # criando um método similar a um get
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.firstName, self.lastName)

    # criando um método similar a um get
    @property
    def fullname(self):
        return '{} {}'.format(self.firstName, self.lastName)

    @fullname.setter
    def fullname(self, name):
        firstName, lastName = name.split(' ')
        self.firstName = firstName
        self.lastName = lastName

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.firstName = None
        self.lastName = None


emp_01 = EmployeePD('Heitor', 'Camara')
print(emp_01.fullname)
print(emp_01.email)
# Não é permitido (sem a existÊncia de um método set definido)
# emp_01 = 'Teste.Email@company.com'
# emp_01.fullname = 'Novo Nome da Silva'

# mudando a propriedade firstName
emp_01.firstName = 'Andre'
print(emp_01.fullname)
print(emp_01.email)

# usando o método set fullname
emp_01.fullname = 'Mateus Azevedo'
print('Nome completo:', emp_01.fullname)
print('Email:', emp_01.email)

# usando o método para exclusão do nome completo
del emp_01.fullname
print(emp_01.fullname)

emp_01.fullname = 'John Smith'
print('Nome completo:', emp_01.fullname)
print('Email:', emp_01.email)
