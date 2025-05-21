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

# If Conditional Statement in Python
# Ex - 1 
age = 20 
if age >= 18:
    print ("Eligible for vote ")

    # If else Conditional Statements in Python
    my_age = 10
    if my_age >= 12:
        print("Eligable for Travle ")
    else:
        print("Not Eligiable for travle")

        # elif Statement

    age = 38
    if age <= 5:
        print ("infant")
    elif age <= 6:
        print ("Child")
    elif age <= 15:
        print ("Teenage")
    elif age <= 25 :
        print ("adult")
    else:
        print ("Oldage")



