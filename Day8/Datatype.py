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

########################################################################
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


###############################################################################
# List Data Type
# A list is an ordered, mutable (changeable) collection that allows duplicate elements.
# It is one of the most commonly used data types in Python.
# Lists are just like arrays, declared in other languages which is an ordered 
# collection of data. 
# It is very flexible as the items in a list do not need to be of the same type.
# Creating a List in Python

# Lists in Python can be created by just placing the sequence inside the square brackets[].
# Empty list
a = []

# list with int values
a = [1, 2, 3]
print(a)

# list with mixed int and string
b = ["Anshu", "Pune", "Infosys", 4, 5]
print(b)


##########################################################################
# Tuple Data Type
# Just like a list, a tuple is also an ordered collection of Python objects. 
# The only difference between a tuple and a list is that tuples are immutable. 
# Tuples cannot be modified after it is created.
# Creating a Tuple in Python

# In Python Data Types, tuples are created by placing a sequence of values 
# separated by a ‘comma’ with or without the use of parentheses for grouping 
# the data sequence. Tuples can contain any number of elements and of any datatype
#  (like strings, integers, lists, etc.).

empty_tuple = ()
numbers = (1, 2, 3, 4)
mixed = (1, "Anshu", True, 3.14)
nested = (1, [2, 3], (4, 5))

print (empty_tuple)
print (numbers)
print(mixed)
print (nested)


#######################################################################
# Why Use Tuples?
# To protect data from being modified

# Tuples use less memory and are faster than lists

# Ideal for fixed data sets like days of the week, coordinates, config settings

########################################################################