# Example 1 
# There are two friends, John and Smith, and the parameters j_angry and 
# s_angry to indicate if each is angry.
# You are in trouble if both of them are angry or no one of them is angry.

def in_trouble(j_angry, s_angry):
    if j_angry and s_angry:
        # Both are angry
        return True
    elif not j_angry and not s_angry:
        # Neither is angry
        return True
    else:
        # One is angry, the other is not
        return False
print(in_trouble(True, True))    # ➜ True (Both angry)
print(in_trouble(False, False))  # ➜ True (Neither angry)
print(in_trouble(True, False))   # ➜ False (Only John angry)
print(in_trouble(False, True))   # ➜ False (Only Smith angry)


#########################################################################
# Example 2 
# Mark Even and Odd - Python
# Given a positive integer x. Your task is to check, if it is even or odd 
# (Any number that gives zero as remainder when divided by 2 is an even number)
x = int (input("Enter a number : "))
if x % 2 == 0:
    print ( "Given Number is Even " )
else:
    print ("Given number is Odd")

#############################################################################
# Example -3 
# Given two integer variables a and b, and a boolean variable flag. 
# The task is to check the status and return accordingly.

# Return True for the following cases:

# Either a or b (not both) is non-negative and the flag is false.
# Both a and b are negative and the flag is true.
# Otherwise, return False.

def check_status(a, b, flag):
    if (flag and a < 0 and b < 0):
        return True
    elif (not flag) and ((a >= 0 and b < 0) or (a < 0 and b >= 0)):
        return True
    else:
        return False
    
print(check_status(-5, -6, True))    # ➜ True (both negative and flag is True)
print(check_status(5, -6, False))    # ➜ True (only one non-negative and flag is False)
print(check_status(-5, 6, False))    # ➜ True
print(check_status(5, 6, False))     # ➜ False (both non-negative, flag is False)
print(check_status(-5, 6, True))     # ➜ False (flag is True but both not negative)

#################################################################################
# Example 4 
# Question 
# You are given a string str, you need to return True if  the words 
# "cat" and "hat"
#  appear same number of times in str, otherwise return False.

def cat_hat_equal(str): # Define Function
    cat_count = str.count("cat") # Count the number of times "cat" appears
    hat_count= str.count("hat") # Count the number of times "Hat" appears
    return cat_count == hat_count # Return True if both counts are equal, otherwise False
print(cat_hat_equal("cat and hat"))   # Output True  
print (cat_hat_equal('cat are cat not hat')) #Output False
print (cat_hat_equal("hat is hat not cat ")) # Output False

#################################################################################
# Example 5
# Question--- Given an integer a, you have to use the if statement to print 
# "Big" (without quotes) if the given number is greater than 100, and use the 
# else statement to print "Number" (without quotes) when the number is smaller 
# than or equal to 100.
# Note: After printing the output, you should move the cursor to the new line.

x = int(input("Print a Number : "))
if x >= 100:
    print ("Big")
else:
    print ("Number")
#######################################################################
# Example - 6
# Question ---
# You are given a number a and you have to print your answer according to 
# the following:

# If the number is divisible by 3, you print "Fizz" (without quotes)
# If the number is divisible by 5, you print "Buzz" (without quotes)
# If the number is divisible by both 3 and 5, you print "FizzBuzz" (without quotes)
# In any other case, you print the number itself
# Note: You should add a new-line character after print statement.   
# 
a = int(input("Please provide a Number : "))
if a%3 == 0 and a%5 == 0:
    print ("FizzBuzz")
elif a%3 == 0:
    print("Buzz")
elif a%5 == 0:
    print ('Fizz')
else:
    print (a)

 ######################################################################
 # Example 7 
 # Question --- 
 # Given a number n, number of apples in a bag. You and your friend are 
 # picking one apple turnwise from the bag. It is given that the first attempt 
 # is always by you. The person picking the last apple will be the winner. 

# If you will win: print "You" (without quotes)
# If your friend will win: print "Friend" (without quotes)   

n = int(input("number of apple : " ))
if n % 2 == 1 :
    print ("You are the winner - Anshu")
else:
    print ("Your Friend is winner - Anshu ")

###################################################################

m = int(input(" Please choose a number :  "))
if m % 2 == 1:
    print ("odd")
else:
    print("Even")
