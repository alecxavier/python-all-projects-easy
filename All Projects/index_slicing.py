import random
import string
import sys

# x = 'Here is a short sample text and this is my string.'
# x.upper()

# alec = x.split()
# # print(alec)   


# capitalism = "Capitalism is an economic system based on the private ownership of the means of production and their operation for profit. Central characteristics of capitalism include capital accumulation, competitive markets, a price system, private property and the recognition of property rights, voluntary exchange and wage labor. In a capitalist market economy, decision-making and investments are determined by every owner of wealth, property or production ability in capital and financial markets whereas prices and the distribution of goods and services are mainly determined by competition in goods and services markets."
# split_capitalism = capitalism.split()


# socialism = "Socialism is a political, social, and economic philosophy encompassing a range of economic and social systems characterised by social ownership of the means of production. It includes the political theories and movements associated with such systems. Social ownership can be public, collective, cooperative, or of equity. While no single definition encapsulates the many types of socialism, social ownership is the one common element. The types of socialism vary based on the role of markets and planning in resource allocation, on the structure of management in organizations, and socialists disagree on whether government, particularly existing government, is the correct vehicle for change."
# split_socialism = socialism.split()

# collect = [split_capitalism, split_socialism]

# brief_capitalism = collect[0][0:20]
# print(brief_capitalism)

# alcc = "Alec Xavier Medina Alba Billy Kimber Hello I am Billy Kimber and I run the races"
# finalalcc = alcc.split()
# finalalcc.reverse()
# print(finalalcc) 


# sweets = {

#     "small": ["m&ms", "maltese", "nerds", "skittles", "jolly"],
#     "medium": ["ferrero rocher", "snickers", "twix", "bounty"],
#     "large": ["toblerone", "dairy milk", "mars", "cool"],

# }

# best_pick = sweets['small'][1]
# print(best_pick)

# sweets["larger"] = ["symere", "python", "nations", "humming"]
# sweets["large"][0] = "Tobleirun"

# print(sweets)


# print("Alec Xavier Medina Alba")
# print("spacing")


# minessotan = "SS Minnesotan was a cargo ship built in 1912 for the American-Hawaiian Steamship Company. During World War I she was known as USAT Minnesotan in service for the United States Army and USS Minnesotan (ID-4545) in service for the United States Navy. She ended her career as the SS Maria Luisa R. under Italian ownership. She was built by the Maryland Steel Company as one of eight sister ships for the American-Hawaiian Steamship Company, and was employed in inter-coastal service via the Isthmus of Tehuantepec and the Panama Canal after it opened. In World War I, USAT Minnesotan carried cargo and animals to France under charter to the U.S. Army from September 1917. When transferred to the U.S. Navy in August 1918, USS Minnesotan continued in the same duties, but after the Armistice she was converted to a troop transport and returned over 8,000 American troops from France. Returned to American-Hawaiian in 1919, Minnesotan resumed inter-coastal cargo service, and, at least twice, carried racing yachts from the U.S. East Coast to California. During World War II, Minnesotan was requisitioned by the War Shipping Administration and initially sailed between New York and Caribbean ports. In the latter half of 1943, Minnesotan sailed between Indian Ocean ports. The following year the cargo ship sailed between New York and ports in the United Kingdom, before returning to the Caribbean. In July 1949, American-Hawaiian sold Minnesotan to Italian owners who renamed her Maria Luisa R.; she was scrapped in 1952 at Bari."

# list_minessotan = minessotan.split()
# set(list_minessotan)

# unfilledPool = 0
# while unfilledPool < 20:
#     conclusion = f"The pool is being filled in progress of {unfilledPool}/20"
#     print(conclusion)
#     unfilledPool = unfilledPool + 1
# else:
#     if unfilledPool == 20:
#         print(f"The pool is now filled {unfilledPool}")


print("\n")
value = random.randint(0, 1)
print(value)
if value == 0:
    print("You have received heads.")
else:
    print("You have received tails.")

drinking = ["ketchup", "water", "orange juice", "mayonnaise", "vinegar", "soy sauce", "pineapple juice"]
randomDrink = random.choices(drinking, weights = [15, 3, 7, 15, 20, 20, 7], k = 2)
print(randomDrink)

print("Practicing with the random module")

first = ['Liam', 'Noah', 'Oliver', 'Elijah', 'William', 'James', 'Benjamin', 'Lucas', 'Henry', 'Alexander', 'Mason', 'Michael', 'Ethan', 'Daniel', 'Jacob' 'Logan', 'Jackson', 'Levi', 'Sebastian', 'Mateo']
last = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzales', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson']
middle = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
street = range(20, 180)
home = ['Greenwood Avenue', 'Princess Road', 'Oak Lane', 'Leigh Road', 'Osborne Road', 'The Maltings', 'Hawthorne Avenue', 'Milton Close', 'Foxglove Close', 'Saxon Road', 'The Crescent', 'Lodge Close', 'Grosvenor Road', 'Willow Road', 'Brookside', 'Teal Close', 'Second Avenue', 'Beverley Close', 'Francis Road', 'Central Avenue']

for num in range(100):
    first_name = random.choice(first)
    last_name = random.choice(last)
    middle_name = f"{random.choice(middle)}."
    phone = f'{random.randint(100,999)}-555-{random.randint(1000, 9999)}'
    street_number = random.choice(street)
    home_address = random.choice(home)
    zip = f"Zip/Postal Code: {random.randint(1000,9999)}"
    email = f"{first_name.lower()}{last_name.lower()}@gmail.com"

    print(f"\n{last_name}, {first_name} {middle_name} \n{phone} \n{street_number} {home_address} \n{zip} \n{email}")

lower = string.ascii_lowercase
print(lower)



uppercase = string.ascii_uppercase
alphabetUpper = random.random(uppercase)

print(alphabetUpper)


nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print("Found!")
        continue
    print(num)

randomNumber = random.randint(0, 100)
randomRes = randomNumber
print(randomRes)

for x in range(1, 101):
    if x < 50:
        print(f"< 50, {x}")
        continue
    elif 75 >= x >= 50:
        print(f"> 50, =< 75, {x}") 
        continue
    elif 100 >= x >= 75:
        print(f"> 75, {x}")
        continue


remainder = []
for x in range(1, 101, 10):
    remainder.append(x**2 %5)

print(remainder)

movies = ["Alec Xavier", "Xavier", "Jewel", "Liam" "Alligator", "Arguelles", "Alice in the Wonderland", "Baxter", "American Psycho"]
g_movies = []
for title in movies:
    if title.startswith("A"):
        g_movies.append(title)

print(g_movies)

