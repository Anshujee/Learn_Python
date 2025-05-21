    ################## Python Data Types  ##################
# Data types in Python define the type of value a variable holds — 
# like whether it's a number, text, list, or something else. 
# Python is dynamically typed, so you don't need to declare data types explicitly.
# Python data types are classes and variables are instances (objects) of these classes. 
# The following are the standard or built-in data types in Python:
# 1.  Numeric - int, float, complex
# 2.  Sequence Type - string, list, tuple
# 3.  Mapping Type - dict
# 4.  Boolean - bool
# 5.  Set Type - set, frozenset
# 6.  Binary Types - bytes, bytearray, memoryview

#################### Discuss some important Data Type ##########################
# 2. Sequence Data Types in Python
# The sequence Data Type in Python is the ordered collection of similar or different Python data types. 
# Sequences allow storing of multiple values in an organized and efficient fashion
# There are several sequence data types of Python:

# Python String
# Python List
# Python Tuple

# String Data Type
# Python Strings are arrays of bytes representing Unicode characters. In Python, 
# there is no character data type Python, a character is a string of length one. 
# It is represented by str class.

# Strings in Python can be created using single quotes, double quotes or even 
# triple quotes. We can access individual characters of a String using index.

s = 'Welcome to the World of Python'
print(s)

# check data type 
print(type(s))

# access string with index
print(s[0])
print(s[1])
print(s[2])
print(s[-1])
print(s[-2])