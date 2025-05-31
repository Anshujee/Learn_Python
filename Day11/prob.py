#########################################################################
#  You are given a number N, you need to print its multiplication table

N = int(input("Enter a Number : - "))
print (f'\n Multiplication Table of {N}:\n')
for i in range (1 , 11):
    print (f"{N} * {i} = {N * i}")

##############################################################################
# Question - You are given a string str, you need to print its characters at even 
# indices(index starts at 0).
# Input string
str = input("Enter a string: ")

# Print characters at even indices
for i in range(0, len(str), 2):

    print(str[i], end= " ")

   

################################################################################
for s in "ANSHU":
    print (s)

#############################################################################

# Increment the sequence with 3 (default is 1):
for r in range (0 ,30, 3):
    print (r)

###############################################################################

# Table of 4 
for table in range (0,42,4):
    print(table)

# range(start, stop, step) Ex - range (0,42,4)
# here start = 0: start from index 0 (first character)
# stop = 42 : 
# step = 4 : skip every second character (i.e., jump 4 steps at a time)

# similarly we can write any table 
##############################################################################

# While loop Peoblem - 

# Given a number count, the task is to print the numbers from x to 0 in 
# decreasing order in a single line.

count = int (input (" Please enter the number : - "))
while count >= 0:
    print (count, end= " ")
    count -= 1 

###################################################################################



# Given a positive integer x, the task is to print the numbers from 1 to x in the order 
# as 1^2, 2^2, 3^2, ... (in increasing order).

x = int (input ("Enter a number : - " ))
m = 1
while m <= x:
    print (m**2, end= " ")
    m += 1 


##############################################################################

y = int (input( "Enter positve Interger : - "))
s = 1
while s ** 2 <= y:
    print (s **2, end= " ")
    s += 1
##############################################################################
# You are given a number n. The number n can be negative or positive. If n is 
# negative, print numbers from n to 0 by adding 1 to n in the neg function. 
# If positive, print numbers from n-1 to 0 by subtracting 1 from n in the pos 
# function.

def pos(n):
   for i in range (n-1 , -1, -1):
       print (i , end= " ")

def neg (n):
    for i in range (n , 1, 1):
        print (i, end= " ")  
        print(0)

def main(n):
    if n==0:
        print ("Already Zero")
    elif n > 0:
        pos (n)
    else:
        neg (n)

main (0)
main(4)
main(-3)

#########################################################################
def multiplication_table(n):
    table = []
    for i in range(1, 11):
        table.append(n * i)
    return table

# Example usage:
n = int(input("Enter a number: "))
result = multiplication_table(n)
print(result)

                
    

       