# Python Variables
# In Python, variables are used to store data that can be referenced 
# and manipulated during program execution. A variable is essentially 
# a name that is assigned to a value. 
# Variables act as placeholders for data. 
# They allow us to store and reuse values in our program.
#Example:


# Variable 'x' stores the integer value 10

x = 5

# Variable 'name' stores the string "Samantha"

name = "Samantha"  

print(x)

print(name)

# Dynamic Typing
# Python variables are dynamically typed, meaning the same variable 
# can hold different types of values during execution.
# In Python, dynamic typing means that the type of a variable is determined 
# at runtime, and you don’t need to explicitly declare the type. 
# The same variable can hold different types of values throughout execution.

x = 10
x = "Now a string"
print (x)
print (x)
# Multiple Assignments
# Python allows multiple variables to be assigned values in a single line.
a = b = c = 240588
print (a,b,c)
# Assigning Different Values
# We can assign different values to multiple variables simultaneously, 
# making the code concise and easier to read.
x, y, z = 1, 2.5, "Anshu"
print(x, y, z)

# Type Casting a Variable
# Type casting refers to the process of converting the value of one data type 
# into another. Python provides several built-in functions to facilitate casting, 
# including int(), float() and str() among others.
# Type Casting Example
x = "24"
print(type(x))
y = "25"
print(float(y))
y = 400
print(float(y))
age = 35
print(str(age))

z = (str(age))
print(z)
a = float(z)
print (a)
# Getting the Type of Variable
# In Python, we can determine the type of a variable using the type() function. 
# This built-in function returns the type of the object passed to it.
# Example Usage of type()
# Define variables with different data types
n = 42
f = 3.14
s = "Hello, World!"
li = [1, 2, 3]
d = {'key': 'value'}
bool = True

# Get and print the type of each variable
print(type(n))   
print(type(f)) 
print(type(s))   
print(type(li))     
print(type(d))     
print(type(bool))

# Scope of a Variable
# There are two methods how we define scope of a variable in python 
# which are local and global.

# Global and Local Variables in Python
# Global Variables
# These are those which are defined outside any function and which are 
# accessible throughout the program, i.e., inside and outside of every function.
x = "Anshu" # Global Variable 
def function(): # Defining the Function
    print ("Print Inside Function",x) # Print statment inside function 
function() # Calling a function 

print ("Print Outside Function",x)

# So here in above example x is work as a global variable and is used in both 
# Ouside and Inside the function. 


    




