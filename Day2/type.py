# Type Function in Python 

# What is the type() Function?
# Imagine you are organizing your fridge.
# You have milk, eggs, fruits, and vegetables. 
# You want to know what type of item each one is. 
# Similarly, in Python, the type() function helps you identify the 
# type of a variable or value.

# It tells what kind of data is stored in a variable,
# just like labels on food packages help you understand 
# what you're eating!

# The syntax of type() is very simple:
# It takes an object (variable, value, or expression) as an argument and returns its data type.
# Example 1: Checking the Type of a Variable
x = 10
print(type(x))  # Output: <class 'int'>

y = 3.14
print(type(y))  # Output: <class 'float'>

name = "Anshu"
print(type(name))  # Output: <class 'str'>

# Example 2: Using type() with Different Data Types
# List
my_list = [1, 2, 3]
print(type(my_list))  # Output: <class 'list'>

# Tuple
my_tuple = (10, 20, 30)
print(type(my_tuple))  # Output: <class 'tuple'>

# Dictionary
my_dict = {"name": "Anshu", "role": "DevOps"}
print(type(my_dict))  # Output: <class 'dict'>

# Boolean
status = True
print(type(status))  # Output: <class 'bool'>

# The type() function is a simple yet powerful tool in Python. 
# Whether you're writing DevOps automation scripts, testing APIs, 
# or debugging applications, type() helps ensure data correctness and prevents 
# unexpected errors.