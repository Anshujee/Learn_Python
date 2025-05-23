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
# Question
# You are given a string str, you need to return True if  the words 
# "cat" and "hat"
#  appear same number of times in str, otherwise return False.

def cat_hat_equal(str):
    cat_count = str.count("cat")
    hat_count= str.count("hat")
    return cat_count == hat_count
print(cat_hat_equal("cat and hat"))
print (cat_hat_equal('cat are cat not hat'))
print (cat_hat_equal("hat is hat not cat "))

 
    


