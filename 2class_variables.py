class Employee:

    raise_amount = 1.04
    no_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower()+'.'+last.lower()+'@company.com'
        # self.no_of_emps+=1 # This would increment at the instance level
        Employee.no_of_emps+=1 # This would increment at the class level
                               # and not at the instance level.

    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    # def apply_raise(self):
    #     self.pay = int(self.pay * 1.04)

    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)


print(Employee.no_of_emps)
emp1 = Employee('Foo', 'Boo', 60000)
emp2  =Employee('Zoo', 'Choo', 50000)
emp1.apply_raise()
print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)
emp1.raise_amount = 1.05
print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)
print(Employee.no_of_emps)
print(emp1.no_of_emps) # For increment at instance level
print(emp2.no_of_emps) # For increment at instance level












