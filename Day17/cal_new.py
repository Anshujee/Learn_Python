# In this programm we will create a simple calculator that can perform basic arithmetic operations like addition, subtraction, multiplication
# Using Command Line Interface (CLI)
import sys

def add(a,b):
    addition = a + b
    return  addition
def subtract(a,b):
    sub = a - b
    return  sub
def multiply(a,b):
    mul = a * b
    return  mul

a = float(sys.argv[1]) # first argument is the operation
opration = sys.argv[2] # second argument is the first number
b = float(sys.argv[3]) # third argument is the second number

if opration == 'add':
    output = add(a,b)
    print("Output :", output)
elif opration == 'sub':
    output = subtract(a,b)
    print("Output :", output)
elif opration == 'mul':
    output = multiply(a,b)
    print("Output :", output)
