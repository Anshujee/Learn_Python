# Ask the user to enter two numbers
num1 = float(input("Enter first number: "))  
num2 = float(input("Enter second number: "))  

# Ask the user to choose an operation
operation = input("Choose operation (+, -, *, /, %, **): ")  

# Perform the chosen operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        result = "Error! Division by zero is not allowed."
    else:
        result = num1 / num2
elif operation == "%":
    result = num1 % num2
elif operation == "**":
    result = num1 ** num2
else:
    result = "Invalid operation!"

# Print the result
print("Result:", result)