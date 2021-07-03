#FIle Object

#!  open('filename.filetype', 'mode')
#!  'mode' can be 'r', 'w', 'a', 'rb', 'wb'
#!  'r' mode can be used with read(), readline(), readlines()
#!  'w' mode can be used with write(), writeline()
#!  'rb' mode is read binary, can be used to read code that is not a char
#!  'wb' mode is write binary, can be used to write code that is not a char
#!  end="" is placed at the end of the string, something like that.

#! variable = open('filename.filetype', 'r')
#! print(variable.name)
#! print(variable.mode)
#! variable.close()

with open("python.py", "r") as pythonFile:
    with open("pythonCopy.py", "w") as pythonFileCopy:
        for content in pythonFile:
            pythonFileCopy.write(content)


#this is a comment