


import random

#! Currently learning all about File Writing and Reading and maybe appending.

filetype = 'py'
list1 = ["name", "black", "white", "weight", "trick", "fungi", "radical", "left"]


pyfile = []
for i in range(1, 21):
    if len(pyfile) < 21:
        pyfile.append(f"{random.choice(list1)}{random.randint(0, 100)}.{filetype}")
    elif len(pyfile) > 20:
        break

with open("samplePython.py", "r") as sample:
    with open(f"{random.choice(pyfile)}", "w") as new:
        for lines in sample:
            new.write(lines)

