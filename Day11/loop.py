# Loops in Python - For, While and Nested Loops
# For loop
# A for loop in Python is used to iterate (loop) over a sequence like a list,
# tuple, string, or range of numbers. It allows you to repeat a block of code 
# for each item in that sequence.
# Basic Syntax:

# for variable in sequence:
    # code block to execute
# variable – A name used to represent the current element in the sequence.

# sequence – Any iterable object (e.g., list, string, range, tuple).

# The indented block under for runs for each item in the sequence.

# Example 1: Looping through a list of DevOps tools
tools = ["linux","AWS","AZURE","Docker","Kubernetes","Terraform",
         "Networking","Git","Ansebel"]
for tool in tools:
    print("For DevOps Learn ", tool)
    
########################################################################
# Example 2: Looping through a range of numbers
for i in range (5):
    print (i)

########################################################################

# for loop with break, continue, and else

# break – Exit the loop early
# Use break when you want to stop the loop as soon as a condition is met.
# Example: Stop scanning servers if one is down

    server = ["UP", "UP", "Down","UP"]
for status in server:
    if status == "Down":
        print ("Server is down. Stopping check!")
        break
    print ("Server is Healthy") 


    #################################################################################

    # continue – Skip current iteration and move to next
    # Use continue when you want to skip a particular condition but continue looping.
    # Example: Skip already updated servers

    server1 = ["updated","updated","pending","updated"]
    for status in server1:
        status == "updated"
        continue
    print("Sever need to update : ", status)

    ########################################################################

    # else – Runs when loop completes normally (no break)
    # The else block after a for loop runs only if the loop wasn't broken with break.


              


