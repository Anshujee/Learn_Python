############# Recursion in Python ######################################
# RECURSION is a programming technique where a function calls itself to solve a problem. 
# It is often used to solve problems that can be broken down into smaller, similar subproblems.
# Recursion is a programming technique where a function calls itself to solve a problem.

# Think of it as "divide and conquer": the function breaks the problem into smaller
# versions of itself until it reaches a simple case (called the base case) and then works its way back up.
# Recursion can be a powerful tool, but it can also lead to performance issues if not used carefully.
# Syntax of a recursive function:
def recursive_function(parameters):
    if base_case_condition:  # Base case
        return base_case_value
    else:
        return recursive_function(modified_parameters)  # Recursive case
#############################################################################################
# Here are some examples of recursion in Python:
def factorial(n):
    """Calculate the factorial of a number using recursion."""
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case
    print(factorial(5))  # Output: 120
#############################################################################################
def fibonacci(n):
    """Calculate the nth Fibonacci number using recursion."""
    if n <= 0:  # Base case
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case
    
print(fibonacci(10)) # Output: 55


