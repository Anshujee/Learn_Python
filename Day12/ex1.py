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