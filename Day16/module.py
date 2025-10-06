# Module In Python : In Pyhotn module is a file containing Python code. 
# It can define functions, classes, and variables that you can 
# reuse in other Python programs. 
# Modules help organize code and promote code reusability.

# Creating a Module
def greet(name):
    return f"Hello, {name}!"
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
print (greet("Anshu"))
print (add(5, 3))
print (subtract(10, 4))
print (multiply(2, 6))

# Using a Module
# To use a module in another Python file, you can use the import statement.
import module  # Assuming the module is saved as module.py
print(module.greet("Anshu Jee"))
print(module.add(5, 3))
print(module.subtract(10, 4))
print(module.multiply(2, 6))
