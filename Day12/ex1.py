######################################################################
""" Given a number n, find the sum of the first n natural numbers.
"""
# Example -1

def sum_of_natural_numbers(n):
    """"
    Calculate the sum of the first n natural numbers.
    
    :param n: The number of natural numbers to sum.
    :return: The sum of the first n natural numbers.
    """
    return n * (n + 1) // 2
n = int(input("Enter a natural number: "))
result = sum_of_natural_numbers(n)
print(f"The sum of the first {n} natural numbers is: {result}")

############################################################################

# Example -2
# Same Problem with different approach using loop approch
def sum_of_natural_numbers_loop(n):
    """
    Calculate the sum of the first n natural numbers using a loop.
    
    :param n: The number of natural numbers to sum.
    :return: The sum of the first n natural numbers.
    """
    if n < 1:
        return "Please enter a natural number (1 or greater)."
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
n_loop = int(input("Enter a natural number for loop approach: "))
result_loop = sum_of_natural_numbers_loop(n_loop)
print(f"The sum of the first {n_loop} natural numbers using loop is: {result_loop}")

#############################################################################

# Example -3
# Given two number n1 and n2, n1 > n2. Find the differences between mathematical tables of n1 and n2 and print in a single line.
def difference_of_tables(n1, n2):
    """
    Calculate the differences between the multiplication tables of n1 and n2.
    
    :param n1: The first natural number.
    :param n2: The second natural number.
    :return: A list of differences between the multiplication tables of n1 and n2.
    """
    differences = []
    for i in range(1, 11):  # Multiplication tables from 1 to 10
        diff = (n1 * i) - (n2 * i)
        differences.append(diff)
    return differences
n1 = int(input("Enter the first natural number (n1): "))
n2 = int(input("Enter the second natural number (n2): "))
if n1 <= n2:
    print("Please ensure that n1 is greater than n2.")
else:
    result_diff = difference_of_tables(n1, n2)
    print(f"The differences between the multiplication tables of {n1} and {n2} are: {result_diff}")

  ################################################################################

#   Example -4
# Given an integer n,  write a program to print the square wall of size n using nested loops. Try not to use String multiplication.
def print_square_wall(n):
    """
    Print a square wall of size n using nested loops.
    
    :param n: The size of the square wall.
    """
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()  # Move to the next line after each row
n_square = int(input("Enter the size of the square wall: "))
print_square_wall(n_square)
################################################################################

# Example -5
# Given an integer n. Write a program to print the Right angle triangle wall. 
# The length of perpendicular and base is n.  
# Use single loop and string multiplication.

# Note: Print exactly single " " after "*". 
# Print a new line after printing the triangle.
def print_right_angle_triangle(n):
    """
    Print a right angle triangle of size n using string multiplication.
    
    :param n: The height of the triangle.
    """
    for i in range(1, n + 1):
        print("* " * i)  # Print i stars followed by a space
n_triangle = int(input("Enter the height of the right angle triangle: "))
print_right_angle_triangle(n_triangle)
################################################################################

# Example -6
# Given an integer n. Write a program to print the Right angle triangle. 
# The length of the perpendicular and base is n.  
# Use nested loops and string multiplication.   
def print_right_angle_triangle_nested(n):
    """
    Print a right angle triangle of size n using nested loops.
    
    :param n: The height of the triangle.
    """
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()  # Move to the next line after each row
n_triangle_nested = int(input("Enter the height of the right angle triangle (nested): "))
print_right_angle_triangle_nested(n_triangle_nested)
##################################################################################
# Example -7
# Given an integer n. Write a program to print the inverted "Right angle triangle" wall. The length of the perpendicular and base is n.
def print_inverted_right_angle_triangle(n):
    """
    Print an inverted right angle triangle of size n.
    
    :param n: The height of the triangle.
    """
    for i in range(n, 0, -1):
        print("* " * i)  # Print i stars followed by a space
n_inverted_triangle = int(input("Enter the height of the inverted right angle triangle: "))
print_inverted_right_angle_triangle(n_inverted_triangle)
##################################################################################
# Example -8
# Given an integer n. Write a program to print all the divisors of n in a single line.
def print_divisors(n):
    """
    Print all the divisors of n in a single line.
    
    :param n: The number to find divisors for.
    """
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors
n_divisors = int(input("Enter a natural number to find its divisors: "))
result_divisors = print_divisors(n_divisors)
print(f"The divisors of {n_divisors} are: {result_divisors}")
##################################################################################
# Example -9
# Given a positive integer, n. Find the factorial of n.
def factorial(n):
    """
    Calculate the factorial of a positive integer n.
    
    :param n: The number to calculate the factorial for.
    :return: The factorial of n.
    """
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
n_factorial = int(input("Enter a positive integer to find its factorial: "))
result_factorial = factorial(n_factorial)
print(f"The factorial of {n_factorial} is: {result_factorial}")
##################################################################################
# Example -10
# Given a non-negative integer n, your task is to find the nth Fibonacci number.
def fibonacci(n):
    """
    Calculate the nth Fibonacci number.
    
    :param n: The position in the Fibonacci sequence.
    :return: The nth Fibonacci number.
    """
    if n < 0:
        return "Fibonacci is not defined for negative numbers."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
n_fibonacci = int(input("Enter a non-negative integer to find its Fibonacci number: "))
result_fibonacci = fibonacci(n_fibonacci)
print(f"The {n_fibonacci}th Fibonacci number is: {result_fibonacci}")
##################################################################################

