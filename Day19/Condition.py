# This is a simple code to learn about conditions in Python
# 1 if statement
# The if statement is used to execute a block of code if a specified condition is True. If the condition is False, the code block is skipped.
# Example:
x = 10
if x > 5:
    print("x is greater than 5")

# 2 if-else statement
# The if-else statement is used to execute one block of code if a specified condition is True, and another block of code if the condition is False.
# Example:
y = 3
if y > 5:
    print("y is greater than 5")
else:
    print("y is not greater than 5")

# 3 if-elif-else statement
# The if-elif-else statement is used to check multiple conditions. 
# If the first condition is True, its block of code is executed. 
# If not, the next condition is checked, and so on. If none of the conditions are True, 
# the else block is executed.
# Example:
z = 7
if z > 10:
    print("z is greater than 10")
elif z > 5:
    print("z is greater than 5 but not greater than 10")
else:
    print("z is not greater than 5")

# 4 Nested if statements
# You can also nest if statements inside other if statements to 
# check multiple conditions.
# Example:
a = 15
if a > 10:
    if a < 20:
        print("a is between 10 and 20")
    else:
        print("a is greater than or equal to 20")
else:
    print("a is less than or equal to 10")

