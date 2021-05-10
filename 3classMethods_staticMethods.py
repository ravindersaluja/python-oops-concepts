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

    # Creating a class method, above were instance methods/regular methods
    # Below is a decorator
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # Usually start with from #alt constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # These don't work on instance or the class
    @staticmethod
    def is_workday(day):
        # if day.weekday() == 5 or day.weekday()==6:
        if any([day.weekday()==5, day.weekday()==6]):
            return False
        return True

print(Employee.no_of_emps)
emp1 = Employee('Foo', 'Boo', 60000)
emp2 = Employee('Zoo', 'Choo', 50000)
# emp1.apply_raise()
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

Employee.set_raise_amt(1.05)
# Above, same as,
# Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

# Below not so common and doesn't really make sense although the o/p
# is the same
emp1.set_raise_amt(1.06)
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

# Using Class methods as alt constructors

emp_str_1 = 'Foo-Boo-60000'
emp_str_2 = 'Zoo-Choo-50000'

first, last, pay = emp_str_1.split('-')
new_emp1 = Employee(first, last, pay)
print(new_emp1.email)

# With from_string

new_emp2 = Employee.from_string(emp_str_2)
print(new_emp2.email)


# ----------------
# Static Methods
# ----------------

import datetime

my_date = datetime.date(2021, 5, 3)

# print(my_date.weekday())
print(Employee.is_workday(my_date))










