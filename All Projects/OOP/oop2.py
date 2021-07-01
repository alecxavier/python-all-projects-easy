
import datetime
import random

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    #! With the property decorator you can use a regular method like an attribute
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith')
emp_1.first = 'Jobberscotch'



print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

