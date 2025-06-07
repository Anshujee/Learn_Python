############### Concept of Local and Global Variables ###############
# Local variable - a variable that is defined within a function and can only be accessed within that function.
# Scope of a local variable is limited to the function in which it is defined.
# Means that it cannot be accessed outside the function.
# usage: use local variables when you want to use a variable only within a function.
# it is a temporary variable that is used only within a function.
################################################################################################################
# Example: Local variable
def local_variable_example():
    local_var = "I am a local variable"
    print(local_var)
local_variable_example()
################################################################################################################

# Example : 
def add (a,b):
    a = 5
    b = 10
    print(a+b) # Local variable 
add(1 ,2)  # Output: 15
def substract(a, b):
    print(a - b)  # Local variable
substract(10, 5)  # Output: 5

################################################################################################################
# Global variable - a variable that is defined outside of any function and can be accessed from anywhere in the code.

# Scope of a global variable is the entire program.
# Means that it can be accessed from anywhere in the code.
# usage: use global variables when you want to use a variable across multiple functions.
# it is a permanent variable that is used across multiple functions.
# Modifying a global variable inside a function requires the use of the `global` keyword.
################################################################################################################
# Example: Global variable
global_var = "I am a global variable"
def global_variable_example():
    print(global_var)
global_variable_example()  # Output: I am a global variable
################################################################################################################
# Example: Modifying a global variable inside a function
def modify_global_variable():
    global global_var  # Declare the variable as global
    global_var = "I am a modified global variable"
    print(global_var)   
modify_global_variable()  # Output: I am a modified global variable
print(global_var)  # Output: I am a modified global variable
################################################################################################################
# Example: Using global variable in multiple functions
def function1():
    global global_var
    global_var = "Modified in function1"
    print(global_var)
def function2():
    global global_var
    print(global_var)  # Access the modified global variable
function1()  # Output: Modified in function1
function2()  # Output: Modified in function1
################################################################################################################
# Simple Example:
a = 5
b = 10
def add_numbers():
    global a, b  # Declare a and b as global variables
    return a + b
def subtract_numbers():
    global a, b  # Declare a and b as global variables
    return a - b
def multiply_numbers():
    global a, b  # Declare a and b as global variables
    return a * b    
print("Addition:", add_numbers())  # Output: Addition: 15
print("Subtraction:", subtract_numbers())  # Output: Subtraction: -5
print("Multiplication:", multiply_numbers())  # Output: Multiplication: 50
################################################################################################################
