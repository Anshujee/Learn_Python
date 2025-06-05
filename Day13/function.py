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