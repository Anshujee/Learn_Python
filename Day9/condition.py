################## Conditional Statements in Python ######################

# Conditional statements in Python are used to execute certain blocks of code 
# based on specific conditions. These statements help control the flow of a 
# program, making it behave differently in different situations.

# What Are Conditional Statements?
# Conditional statements allow you to control the flow of your program based on conditions (true/false logic).
#  They're essential for decision-making in Python.

# Types of Conditional Statements
# Statement	                      Description
# if	                          Executes a block if condition is true
# if-else	                      Executes one block if true, another if false
# if-elif-else	                  Checks multiple conditions in sequence
# Nested if	                      if inside another if

################################################################################
# If Conditional Statement in Python
# Ex - 1 
age = 20 
if age >= 18:
    print ("Eligible for vote ")

    # If else Conditional Statements in Python
    my_age = 12

    if my_age >= 12:
        print("Eligable for Travle ")
    else:
        print("Not Eligiable for travle")


###############################################################################
        # Example of elif Statement in Python

    age = 6

    if 0 <= age <= 5:
        print ("infant")
    elif  6 <= age <= 14:
        print ("Child")
    elif 15 <= age <= 24:
        print ("Teenage")
    elif age <= 25 :
        print ("adult")
    else:
        print ("Oldage")
##########################################################################

# Nested if..else Conditional Statements in Python

# Nested if..else means an if-else statement inside another if statement. 
# We can use nested if statements to check conditions within conditions.
# A nested if...else is when an if or else block contains another if...else 
# statement inside it.

# 📘 Definition:
# A nested if...else allows you to check multiple levels of conditions. 
# This is useful when decisions depend on more than one condition or hierarchy 
# of checks.

######################################################################
# Example nested if -else
age = 55
is_member = True
if is_member:
 if age >= 65:
    print ("Eligible for Discount of 30 %")
 else:
     print ("Eligible for discount of 20%")
 
else:
    print ("Not eligible for a senior discount.")

#########################################################################
# Ternary Conditional Statement in Python
# A ternary conditional statement is a compact way to write an if-else condition 
# in a single line. 
# It’s sometimes called a "conditional expression."
# Assign a value based on a condition
# Example -1 
age = 17
s = "Adult" if age >= 18 else "Minor"

print(s)
 





