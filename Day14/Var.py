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

