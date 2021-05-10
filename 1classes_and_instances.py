# class Employee:
#     pass

# emp1 = Employee()
# emp2  =Employee()

# emp1.first = 'Foo'
# emp1.last = 'Boo'
# emp1.email = 'foo.boo@company.com'
# emp1.pay = 60000


# emp2.first = 'Zoo'
# emp2.last = 'Choo'
# emp2.email = 'zoo.choo@company.com'
# emp2.pay = 50000

# print(emp1.email)
# print(emp2.email)

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower()+'.'+last.lower()+'@company.com'
    def fullName(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('Foo', 'Boo', 60000)
emp2  =Employee('Zoo', 'Choo', 50000)
print(emp1.email)
print(emp2.email)
print(emp1.fullName())


# emp1 = Employee('Foo', 'Boo', 60000)
# Below is actully instance.method without actually explicitly 
# defining an instance.
print(Employee('Loo', 'Poo', 78000).fullName())

# The below 2 statements are the same. In the second one, the 
# instance is being passed as an argument - self
print(emp1.fullName())
# or
print(Employee.fullName(emp1))
