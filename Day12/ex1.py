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

