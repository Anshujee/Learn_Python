############################################################################
#  Function in Python
# Functions in Python (Definition, Parameters, Return Values)
#  A function is a named block of reusable code that performs a specific task.
#  Functions help you:
# Avoid code repetition
# Improve readability
# Isolate logic for easier testing and debugging
# A function in python is a block of organized ,resuable code that perform a specific task. 
# Function allow you to break your program into smaller, manageable pieces making it 
# easier to read, maintain, and debug. 
# ##################################################################################
# Function are defined using the def keyword followed by the function name and 
# parentheses and colon.
# The body of the function is indented and contains the code that will be 
# executed when the function is called.
##################################################################################

# Syntax:
# def function_name(parameters):
    # Function body
    # Code to be executed
    #return value  # Optional return statement
###########################################################################
# Example -1
def greet(name):
    """Function to greet a person by name."""
    return f"Hello, {name}!"
print(greet("Anshu"))  # Output: Hello, Anshu!
################################################################################
# Example -2 
def add_num(a,b):
    """Function to add two numbers."""
    return a + b
print(add_num(5,5))
################################################################################
# Types of Functions:
# 1. Built-in Functions: These are functions that come with Python, 
# such as `print()`, `len()`, ` sum() ` etc.
# 2. User-defined Functions: These are functions defined by the user
# to perform specific tasks, like the examples above.
# 3. Lambda Functions: These are small anonymous functions defined using the
#  `lambda` keyword.
###############################################################################
# Example -3
# Create function to find the subtraction of two Numbers
def subtract_num(a, b):
    """Function to subtract two numbers."""
    return a - b
print(subtract_num(10, 5))  # Output: 5
################################################################################
# Example -4 La,mbda Function
# Example of lambda function to find the square of a number
square = lambda x: x * x
print(square(5))  # Output: 25
################################################################################    
############## Parameters and Arguments in Functions ##############################
# Parameters are variables that are defined in the function signature,
# while arguments are the actual values passed to the function when it is called.
# Parameters allow you to pass data into functions, making them more flexible and reusable.

# Basically, parameter are the variables listed inside the parentheses in the function definition,
# they act as placeholders for the values that will be passed to the function when it is called.
# In the above Example -1, `name` is a parameter of the `greet` function.
####################################################################################################
# Arguments are the actual values or data that you pass to the function when you call it.
# In the above Example -1, `"Anshu"` is an argument passed to the `greet` function.
# Arguments can be of any data type, including numbers, strings, lists, or even other functions.

#################################################################################################
######################## Types of Argument  ####################################################
# Positional Arguments: These are the most common type of arguments,and must be passed in the same 
# order as the parameters are defined in the function.
# Example of Positional Arguments : 
def add(a, b):
    """Function to add two numbers."""
    return a + b
print(add(3, 5))  # Output: 8
################################################################################
# Keyword Arguments: These arguments are passed by explicitly specifying the parameter name,
# allowing you to pass them in any order.
# These are agruments that are passed to a function by explicitly specifying the parameter name.
# Example of Keyword Arguments:-
def  introduce (name,age):
    """Function to introduce a person by name and age."""
    return f"My name is {name} and I am {age} years old."  
print(introduce(age=25, name="Anshu"))  # Output: My name is Anshu and I am 25 years old.
#############################################################################################


