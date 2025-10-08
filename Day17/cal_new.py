# In this programm we will create a simple calculator that can perform basic arithmetic operations like addition, subtraction, multiplication
# Using Command Line Interface (CLI)
import sys # import sys module to read command line arguments

def add(a,b): # function to add two numbers
    addition = a + b # add the two numbers
    return  addition # return the result

def subtract(a,b): # function to subtract two numbers
    sub = a - b # subtract the two numbers
    return  sub # return the result

def multiply(a,b): # function to multiply two numbers
    mul = a * b # multiply the two numbers
    return  mul # return the result

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
