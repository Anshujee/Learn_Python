#########################################################################
#  You are given a number N, you need to print its multiplication table

N = int(input("Enter a Number : - "))
print (f'\n Multiplication Table of {N}:\n')
for i in range (1 , 11):
    print (f"{N} * {i} = {N * i}")

##############################################################################

# Input string
str = input("Enter a string: ")

# Print characters at even indices
for i in range(0, len(str), 2):
    print(str[i], end=" ")
