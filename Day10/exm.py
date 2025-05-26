a = int(input("Enter first number : "))
b = int(input("Enter second Number : "))
operator = int(input( 'pleae enter 1 for add , 2 for subtract or 3 for Multiplication  operation : '))
if operator == 1:
    print("Result :" , a+b)
elif operator == 2:
    print ("Result :", a-b)
elif operator == 3:
    z = a * b 
    print (" Result :", a*b)
else:
    print ("Invalid Operation")
##########################################################################
# Example - 4 
# Given two integers n and m. The problem is to find the number closest to n and divisible by m. If there is 
# more than one such number, then output the one having the maximum absolute value.

def closest_divisible(n, m):
    # Find the quotient
    q = n // m

    # Closest number on lower or same side
    n1 = m * q

    # Closest number on the higher side
    if n * m > 0:
        n2 = m * (q + 1)
    else:
        n2 = m * (q - 1)

    # Return the closer one, or the one with greater absolute value if same distance
    if abs(n - n1) < abs(n - n2):
        return n1
    elif abs(n - n1) > abs(n - n2):
        return n2
    else:
        # Equal distance — return the one with greater absolute value
        return n1 if abs(n1) > abs(n2) else n2

# Example usage
n = int(input("Enter n: "))
m = int(input("Enter m: "))
print("Closest number to", n, "that is divisible by", m, "is:", closest_divisible(n, m))


###################################################################################
# Ex _5
# You are given a cubic dice with 6 faces.
#  All the individual faces have a number printed on them. The numbers are in the range 
# of 1 to 6, like any ordinary dice. You will be provided with a face of this cube, your 
# task is to guess the number on the opposite face of the cube.


def dice_prob(n):
    if 1 <= n <= 6:
        return 7 - n
    else:
        return "Invalid face number! Must be between 1 and 6."
face = int (input("Enter the face number (1 to 6): "))
result = dice_prob(face)
print("The number on the opposite face is:", result)

##############################################################################
# Define a Point class to store x and y coordinates
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Function to check if two rectangles overlap
def is_overlapping(L1, R1, L2, R2):
    # If one rectangle is to the left of the other
    if (R1.x < L2.x or R2.x < L1.x):
        return False

    # If one rectangle is above the other
    if (R1.y > L2.y or R2.y > L1.y):
        return False

    return True

# Example usage
L1 = Point(0, 10)  # Top-left corner of rectangle 1
R1 = Point(10, 0)  # Bottom-right corner of rectangle 1

L2 = Point(5, 5)   # Top-left corner of rectangle 2
R2 = Point(15, 0)  # Bottom-right corner of rectangle 2

if is_overlapping(L1, R1, L2, R2):
    print("Rectangles Overlap")
else:
    print("Rectangles Do Not Overlap")

################################################################
# Ex - 6
# Given a tuple arr , print "True" if all elements of tuple
#  are different otherwise print "False".
arr = (1,2,3,4,5)
if len (arr) == len (set(arr)):
    print ("True")
else:
    print("False")
    
    
