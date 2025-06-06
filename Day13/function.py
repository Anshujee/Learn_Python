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
# Default Arguments: These are parameters that have a default value assigned to them. 
# These argument can have default values, which are used if no value is provided when the function is called.
# Example of Default Arguments:
def greet(name="Guest"):
#    """Function to greet a person with a default name."""
  return f"Hello, {name}!"
print(greet())  # Output: Hello, Guest! Here the default value "Guest" is used.
print(greet("Anshu"))  # Output: Hello, Anshu! Here the argument "Anshu" is passed, overriding the default value.
############################################################################################## 
# Variable-length Arguments: These allow you to pass a variable number of arguments to a function.
# They are defined using an asterisk (*) before the parameter name.
def sum_all(*args):
    """Function to sum all provided numbers."""
    return sum(args)
print(sum_all(1, 2, 3, 4, 5))  # Output: 15
################################################################################################################
# Keyword Variable-length Arguments: These allow you to pass a variable number of keyword arguments to a function.
# They are defined using two asterisks (**) before the parameter name.
def print_info(**kwargs):
    """Function to print key-value pairs."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Anshu", age=25, city="Pune")

# Output:
# name: Anshu
# age: 25
# city: Pune
##############################################################################################
# Return Values in Functions:
# Functions can return values using the `return` statement.
# The return statement allows you to send a value back to the caller of the function.
def multiply(a, b):
    """Function to multiply two numbers."""
    return a * b
print(multiply(4, 5))  # Output: 20
##############################################################################################.
# If a function does not have a return statement, it returns `None` by default.
def no_return():
    """Function without a return statement."""
    print("This function does not return anything.")
no_return()  # Output: This function does not return anything.
# The function returns None implicitly.
##############################################################################################
# Advantages of Using Functions:
# 1. Code Reusability: Functions allow you to write code once and reuse it multiple times, reducing redundancy.
# 2. Improved Readability: Functions help organize code into logical blocks, making it easier to read and understand.
# 3. Easier Maintenance: Functions isolate logic, making it easier to update or fix specific parts of the code without affecting the entire program.
# 4. Testing and Debugging: Functions can be tested independently, making it easier to identify and fix issues.
# 5. Modularity: Functions allow you to break down complex problems into smaller, manageable pieces, promoting modular programming.
# 6. Collaboration: Functions enable multiple developers to work on different parts of a program simultaneously, improving collaboration.
# 7. Documentation: Functions can include docstrings, providing clear documentation for their purpose and usage.
# 8. Scope Management: Functions have their own scope, allowing you to manage variable visibility and avoid naming conflicts.
# 9. Performance Optimization: Functions can be optimized independently, improving overall program performance.
# 10. Flexibility: Functions can accept different arguments, making them adaptable to various scenarios.
# 11. Recursion: Functions can call themselves, enabling recursive algorithms for solving complex problems.
# 12. Higher-Order Functions: Functions can accept other functions as arguments or return functions, enabling functional programming techniques.
##############################################################################################
# Conclusion:
# Functions are a fundamental concept in Python programming that allow you to organize code into reusable blocks.
# They enhance code readability, maintainability, and collaboration while promoting modular programming practices.
# Understanding how to define and use functions is essential for writing efficient and effective Python programs.
# By mastering functions, you can create more structured and organized code, making it easier to develop and maintain complex applications.
# Functions are a powerful tool that can greatly enhance your programming skills and productivity.

# In this article, we explored the basics of functions in Python, including their definition, parameters, arguments, return values, and various types of arguments.
# We also discussed the advantages of using functions and how they contribute to better code organization and maintainability.
# Functions are a crucial aspect of Python programming, and mastering them is essential for becoming a proficient Python developer.
# Whether you're writing simple scripts or complex applications, understanding functions will help you write cleaner, more efficient code.
# Remember to practice defining and using functions in your Python projects to reinforce your understanding and improve your coding skills.
################################################################################################################################################

