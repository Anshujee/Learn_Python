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

