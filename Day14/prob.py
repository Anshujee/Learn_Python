##### Some basics problem of Python Functions #####
# Example -1 Create function with the first 10 prime numbers

def first_n_primes(n):
    primes = []
    num = 2  # Starting from the first prime number
    while len(primes) < n:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes
print(first_n_primes(10))  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

################################################################################
# Python program to print first 10 prime numbers

# A function name prime is defined
# using def
def fun(n):
    x = 2
    count = 0
    while count < n:
        for d in range(2, int(x ** 0.5) + 1):  # check divisibility only up to sqrt(x)
            if x % d == 0:
                break  # if divisible, it's not prime, so break the loop
        else:
            print(x)  # prime number
            count += 1
        x += 1

# Driver Code
n = 10

fun(n)
#################################################################################
# Example -2 Create a function to check if a number is prime or not
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print(is_prime(11))  # Output: True
print(is_prime(15))  # Output: False
#################################################################################
# Example -3 Create a function to check if a number is even or odd
def is_even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(is_even_or_odd(10))  # Output: Even
print(is_even_or_odd(7))   # Output: Odd
#################################################################################
# Example -4 Create a function to calculate the factorial of a number
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
print(factorial(5))  # Output: 120
#################################################################################
# Example -5 Create a function to find the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd(48, 18))  # Output: 6
#################################################################################
# Example -6 Create a function to find the least common multiple (LCM) of two numbers
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
print(lcm(4, 6))  # Output: 12
#################################################################################

