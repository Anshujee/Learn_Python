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