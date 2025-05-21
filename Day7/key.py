           ##########  Python Keywords #######
# Keywords in Python are reserved words that have special meanings and 
# serve specific purposes in the language syntax. Python keywords cannot 
# be used as the names of variables, functions, and classes or any other 
# identifier.
####################################################################
# Getting List of all Python keywords
import keyword
# printing all keywords at once using "kwlist()"
print ("The list of Keyword is : " )
print (keyword.kwlist)
# OUTPUT is the list of Keyword 
# The list of Keyword is : 
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
# 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 
# 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
#  'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
############################################################################

# Let's categorize all keywords based on context and understand each with help of example.
#   Category	                      Keywords
# Value Keywords	                 True, False, None
# Operator Keywords	             and, or, not, in, is
# Control Flow Keywords	         if, else, elif, for, while, break, continue, pass, try, except, finally, raise, assert
# Function and Class	         def, return, lambda, yield, class
# Context Management	          with, as
# Import and Module	             import, from, as
# Scope and Namespace	          global, nonlocal
# Async Programming	             async, await



###############################################################################
# Async Programming: async, await
# Async programming allows you to run tasks concurrently, improving efficiency, 
# especially when dealing with I/O-bound operations. The async and await keywords 
# in Python are used to define and manage asynchronous functions.
# async: Used to declare a function as asynchronous, allowing it to run 
# concurrently with other tasks.
##############################################################################
import asyncio
async def fun():
    print ("Hello , Async World ")
asyncio.run(fun())
################################################################################
# await: Used to pause the execution of an async function until the awaited 
# task is complete.

import asyncio
async def main():
    await func()
async def func():
    print ("Hello ! async World ")    
asyncio.run(main ()) 
