class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower()+'.'+last.lower()+'@company.com'

    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)

    
class Developer(Employee):
    
    raise_amount = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay) #Alternative
        self.prog_lang = prog_lang
        
    
class Manager(Employee):
    
    def __init__(self, first, last, pay, employees = None): # Never pass mutable data types like a list or a dict as the default argument
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullName())



dev1 = Developer('Foo', 'Boo', 60000, 'Python')
dev2 = Developer('Zoo', 'Choo', 50000, 'C++')

mgr1 = Manager('Hoo', 'Loo', 90000, [dev1])
# print(mgr1.email)
# mgr1.print_emps()

mgr1.add_emp(dev2)
mgr1.rem_emp(dev1)
mgr1.print_emps()

print(isinstance(mgr1, Employee))
print(isinstance(mgr1, Developer))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))


# print(dev1.email)
# print(dev1.prog_lang)

# print(help(Developer))

# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)














