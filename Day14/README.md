# 🔁 Recursion in Python

## 📖 Introduction

**Recursion** is a programming technique where a function calls itself to solve a problem.  
It is especially useful for problems that can be broken down into smaller, similar subproblems — a strategy often referred to as **"divide and conquer."**

However, recursion must be used carefully to avoid performance issues or infinite loops.

---

## 🧠 Basic Concept

In recursion:

- **Base Case**: The stopping condition.
- **Recursive Case**: The function calls itself with a modified argument, gradually approaching the base case.

---

## 🧾 Syntax

```python
def recursive_function(parameters):
    if base_case_condition:  # Base case
        return base_case_value
    else:
        return recursive_function(modified_parameters)  # Recursive case

def factorial(n):
    """Calculate the factorial of a number using recursion."""
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

print(factorial(5))  # Output: 120

Example 2: Fibonacci using Recursion

def fibonacci(n):
    """Calculate the nth Fibonacci number using recursion."""
    if n <= 0:  # Base case
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

print(fibonacci(10))  # Output: 55
