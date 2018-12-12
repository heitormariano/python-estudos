class EmployeeTwo:
    num_emps = 0
    raise_amount = 1.04

    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = firstName + '.' + lastName + '@company.com'

        EmployeeTwo.num_emps += 1

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

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


import datetime


def get_result_info(result):
    if result == True:
        return 'Dia de trabalho. Produzir!'
    else:
        return 'Não é dia de trabalho. Descansar!'


my_date = datetime.date(2018, 10, 28)
print(my_date)

print('{} [Dia] / {}[Mes] / {}[Ano]'.format(my_date.day,
                                            my_date.month, my_date.year))

print(EmployeeTwo.is_workday(my_date))

result_my_date = EmployeeTwo.is_workday(my_date)
print(get_result_info(result_my_date))

current_date = datetime.date.today()
print(current_date)

result_current_date = EmployeeTwo.is_workday(current_date)
print(get_result_info(result_current_date))
