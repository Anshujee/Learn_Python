#######################################################################
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

name = "Anshu"  

print(x)

print(name)

######################################################################
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

######################################################################

# Multiple Assignments
# Python allows multiple variables to be assigned values in a single line.
a = b = c = 240588
print (a,b,c)
# Assigning Different Values
# We can assign different values to multiple variables simultaneously, 
# making the code concise and easier to read.
x, y, z = 1, 2.5, "Anshu"
print(x, y, z)

#######################################################################

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

#######################################################################

# Getting the Type of Variable
# In Python, we can determine the type of a variable using the type() function. 
# This type() built-in function returns the type of the object passed to it.
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

#######################################################################

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
########################################################################

# Local Variable 
# Python local variables are those which are defined inside a function 
# and their scope is limited to that function only.
# Local variables in Python are those which are initialized inside a 
# function and belong only to that particular function. 
# It cannot be accessed anywhere outside the function.
# Creating local variables in Python
# Example  local Variable ---
def function():
    x = "Anshu"
    y = "I am learning Python"
    print(x)
    print(y)
function()
#########################################################
# Can a local variable be used outside a function?
# If we will try to use this local variable outside the function 
# then let's see what will happen.
#def f():
    #h = "Ayan Verma"
#f()
#print (h)
# It will throw an error 
# Traceback (most recent call last):
  #File "/Users/anshujee/Work/Python_Example/Python_Day_to_Day/Learn_Python/Day5/var.py", line 133, in <module>
#print (_z)
# NameError: name '_z' is not defined. Did you mean: 'z'?

######################################################################
#Real World DevOps Example 
aws_region= "us-east-1" # Global_Variable
def create_ec2_instance():
    instance_type = "t2.micro" #local Variable 
    print (f"Creating Instance in {aws_region} of type {instance_type}")
create_ec2_instance()

# Alternet_way
aws_region = "us-east-1"  # Global variable

def ec2_instance():
    return "t2.micro"  # Return value

instance_type = ec2_instance()
print(f"Creating Instance in {aws_region} of type {instance_type}")

######################################################################


x = 10
def test():
    x = 20
    print(x)

test()
print(x)

 #####################################################
def outer():
    x = "hello"
    def inner():
        nonlocal x
        x = "world"
    inner()
    return x

print(outer())
   
# Real DevOps Use-Case Scenario
# You're writing a Python script to automate EC2 instance creation using Boto3. 
# You have multiple instance types based on environment (dev, test, prod). 
# Use local and global variables properly.
aws_region = "us-east-1"
def create_instance(env):
    if env == "dev":
        instance_type = " t2.large"
    elif env == "test":
        instance_type = "t2.mini"
    elif env == "pro":
        instance_type = "t2.Xlarge"
    else:
        instance_type = "t2 micro"
        
    
    print (f" Creating EC2 instance in {aws_region} with instance type {instance_type}")

create_instance("dev")
create_instance("test")
create_instance("pro")



