import datetime
print(datetime.__file__)


class Breakfast:

    def __init__(self, dish, greens, liquids, time_ate):
        self.dish = dish
        self.greens = greens
        self.liquids = liquids
        self.time_ate = time_ate
        
    def sentence(self):
        return f"What I had for my breakfast today was some {self.dish} with some {self.greens}, and I drank {self.liquids}. I had breakfast at {self.time_ate} am"


#! Instances of a class:

bf1 = Breakfast('Bacon and Eggs', 'Spinach', 'Water', '8:00')
bf2 = Breakfast('Toast', 'Squash', 'Water', '8:20')

bf2.sentence()
bf1.sentence()


class Guns:

    def __init__(self, name, front_sight, muzzle, rear_sight, magazine, grip, trigger, safety, buttstock, weight):
        self.name = name
        self.front_sight = front_sight
        self.muzzle = muzzle
        self.rear_sight = rear_sight
        self.magazine = magazine
        self.grip = grip
        self.trigger = trigger
        self.safety = safety
        self.buttstock = buttstock
        self.weight = weight

    def detailed_orientation(self):
        return f"This is the {self.name}, it has an {self.front_sight}, {self.muzzle}, {self.rear_sight}, with a {self.magazine} and a {self.grip}. It also has a {self.trigger}, a {self.safety}, a {self.buttstock}, and weights {self.weight}"


ak47 = Guns('AK47', 'open sight', 'muzzle brake', 'iron sight', '90/270', 'tight-grip', 'sticky-trigger', 'convenient safety lock', 'wooden buttstock', '5.20 kg')
ar15 = Guns('AR15', 'open sight', 'tight muzzle', 'steel rear-sight', '80/240 mag', 'tight grip', 'mechanical trigger', 'convenient safety switch', 'steel buttstock', '6.45 kg')
m82a1 = Guns('Barret M82A1', 'up to 75x scope', 'wide-spread exhaust muzzle', 'glass sight with a crosshair', '18/108 mag', 'stable and consistent grip', 'mechanical trigger', 'no safety-lock', 'black carbon buttstock', '12.4 kg')


ak47.detailed_orientation()
ar15.detailed_orientation()
m82a1.detailed_orientation()




class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '' + self.last + '@gmail.com'

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)   
        return self.pay 

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def remove_char(cls, string):
        first, last, pay = string.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"
        # return f'{self.fullname()} - {self.email}'

    def __str__(self):
        return f'{self.fullname()} - {self.email}'


class Developer(Employee):
    pass


dev_1 = Developer('Alec', 'Xavier', 50000)
dev_2 = Developer('Andrei', 'Liam', 60000)

print(dev_2.__repr__())
print(dev_2.__str__()) 




print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)























str3 = "Michael-Jackson-90000"
str4 = "MeganThee-Stallion-45000"

emp_1 = Employee('Alec', 'Xavier', 50000)
emp_2 = Employee('Andrei', 'Liam', 60000)
emp_3 = Employee.remove_char(str3)
emp_4 = Employee.remove_char(str4)

print(emp_4.pay)
print(emp_4.email)
emp_3.fullname()

my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))



