
import platform
import math

x = platform.system()
print(x)

y = math.pi
print(y)

def practice_function(greet, first_name):
    return f'{greet} {first_name}! Welcome to your function.'

practice_function('Alec Xavier', 'Hello There!')


def params(*phones, name = "Derrick"):
    return f"You used to call me on my {phones[0]} {phones[4]}, {name}."

params("Samsung", "Apple", "Nokia", "Toyota", "Ntbkk", "Pen", "Nintendo")

#! The *args parameter can be used when younar euncertain of the number of arguments are you going to put in yorngiven parameter.
#! So basically, if you'r eunsure of the quantity of arguments you're going to pass in your parameter, just add a * in your parameter name.

#! To explain mathematically, uncertain of quantity of arguments = add * before parameter.


def params2(cond1, cond2, cond3):
    return f"{cond3} is really good."

params2(cond3 = "Ketchup", cond2 = "Mayo", cond1 = "Soy")


#! When you use the keyword argument the order of your arguments responding to parameters don't matter.


def kwargs(**unlimited_arguments):
    return f"{unlimited_arguments['place']} is a way to use coercion to watch me whip, watch me nae nae."

kwargs(place = "Germany", leader = "Adolf Hitler", leader2 = "Mao Zedong", explain = "It allows for unlimited number of arguments that is in a dictionary format")


def calculate(**a):
    return f"{a['country1']} and {a['country4']} is soon to be the World's Economic Superpower"

calculate(country1 = "China", country2 = "USA", country3 = "Germany", country4 = "France", country5 = "Spain")


def my_function(food):
  for x in food:
    print(x)

fruits = {
    "fruit1": "apple", 
    "fruit2": "banana", 
    "fruit3": "cherry"
    }

my_function(fruits.values())


#!

def tri_recursion(k):
  if (k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

#!



