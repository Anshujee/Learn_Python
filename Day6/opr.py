#########################################################################
                    #    Python Operators
# In Python, operators are special symbols or keywords used to perform operations
# on variables and values. 
# Operators are essential for writing logical, mathematical, and functional code.
# Operators in general are used to perform operations on values and variables. 
##############################################################################
# Types of Operators in Python
#  1 . Arithmetic Operators
#  2.  Comparison Operators
#  3.  Logical Operators
#  4.  Bitwise Operators
#  5.  Assignment Operators
#  6.  Identity Operators and Membership Operators
#############################################################################
# Arithmetic Operators in Python
# Python Arithmetic operators are used to perform basic mathematical 
# operations like addition, subtraction, multiplication and division.
# Example 1 ---
#variable 
a = 5 
b = 10

#Addition 
print ("Addition : ", a+b)

# Substraction
print (" Substaction :", a-b)

# multiplication 
print ("Multiplcation : ", a*b)

# Division 
print ("division : ", a/b)

# Floor Division 
print("Floor Division : ", a//b) # It divides two numbers and returns the largest
                                 #possible integer less than or equal to the result 
                                 # — i.e., it rounds down to the nearest whole number.

# Modulus
print("Modulus:", a%b) # The modulus operator returns the remainder 
                         # after division of one number by another.

# Exponentiation
print("Exponentiation:", a**b)

########################################################################

# Comparison of Python Operators or Relational Operator 
# In Python Comparison of Relational operators compares the values. 
# It either returns True or False according to the condition.
# Example 2 --- 
a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

###############################################################
#   Logical Operators in Python
# Python Logical operators perform Logical AND, Logical OR and Logical NOT operations. 
# It is used to combine conditional statements.
# The precedence of Logical Operators in Python is as follows:

# 1 . Logical not
# 2.  Logical and
# 3.  Logical or
# Example 3 --- 
a = True
b = False
print(a and b)
print(a or b)
print(not a)

###################################################################
# Bitwise Operators in Python
#  Python Bitwise operators act on bits and perform bit-by-bit operations. 
# These are used to operate on binary numbers.

# Bitwise Operators in Python are as follows:

# 1.Bitwise NOT
# 2.Bitwise Shift
# 3.Bitwise AND
# 4.Bitwise XOR
# 5.Bitwise OR

a = 10
b = 4

print(a & b) 
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

#Output
#0
# Explanation print(a & b) → Bitwise AND
# a = 1010
# b = 0100
# ----------
# a & b = 0000 → 0 # Thus Output is 0 .
##############################################
# Output
#14 
# Explanation print(a | b) → Bitwise OR
# a = 1010
# b = 0100
#----------
# a | b = 1110 → 14 Thus Output is 14 . 
################################################
#output
# -11  
# print(~a) → Bitwise NOT
# Bitwise NOT flips all bits.
# In Python, this works on signed integers using two's complement.
# a = 10
# ~a = -11 Thus Output is -11. 
##############################################################
# Output 
#14
# print(a ^ b) → Bitwise XOR
# a = 1010
# b = 0100
# ----------
# a ^ b = 1110 → 14 Thus Output is 14 . 
##########################################################
# Output 
#2
# print(a >> 2) → Right Shift by 2
# Shifts bits of a right by 2 positions:
# a = 1010 → becomes 0010 → 2 Thus Output is 2.
###########################################################
#Output
#40
# print(a << 2) → Left Shift by 2
# Shifts bits of a left by 2 positions:
# a = 1010 → becomes 101000 → 40 hus Output is 40. 

###################################################################
# Assignment Operators in Python
# Python Assignment operators are used to assign values to the variables. 
# This operator is used to assign the value of the right side of the 
# expression to the left side operand.
a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a # <<= is a bitwise left shift and assignment operator.
        # It  shifts the bits of b to the left by a positions 
        # and assigns the result back to b.
print(b)
#################################################################
# Identity Operators in Python
# In Python, is and is not are the identity operators both are used to 
# check if two values are located on the same part of the memory. 
# Two variables that are equal do not imply that they are identical. 
# is          True if the operands are identical 
# is not      True if the operands are not identical 

a = 10
b = 20
c = a

print(a is not b)
print(a is c)

#########################################################################
# Membership Operators in Python
# n Python, in and not in are the membership operators that are used to test 
# whether a value or variable is in a sequence.

# in            True if value is found in the sequence
# not in        True if value is not found in the sequence

x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")
#####################################################################