print ("hello world!") # print statement with double quetes.
print ('hello Anshu') # print statement with single quetes.
print ('hello anshu')
print (' I am start learning python by myself\n hello anshu')
# By using (\n) we can print the staement in next line without 
# using print staement again and again 
print ("Hi\nI am Anshu\nI am learing Python\nIt is very good to learn python to upskill. ")

# Concept of Concatenation in Python
#Concatenation in Python refers to the process of joining two or more strings, 
# lists, or tuples using the + operator or specific methods depending on the data type.
# Example - 
# 1. String Concatenation
print('hello'+ 'Anshu')
print ('Hello'+ ' '+'Anshu')
first_name = "Anshu"
last_name = "Jee"
full_name = first_name + " " + last_name
print(full_name)

# Example 2: String Concatenation Using join() Method
words = ["Hello", "world", "!"]
sentence = " ".join(words)
print(sentence)
# The join() method is more efficient when concatenating multiple strings in a list.
# List Concatenation
# Concatenation can also be used to merge two lists.

# Example 3: List Concatenation Using + Operator

list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print(merged_list)

# Tuple Concatenation
# Like lists, tuples can also be concatenated.

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print(merged_tuple)

# Why Do We Use Concatenation?
# Concatenation is used when we need to combine multiple values to 
# form a meaningful output. Some real-world applications include:
# Creating SQL Queries Dynamically - Real World Use Case - Example-

table_name = "employees"
query = "SELECT * FROM " + table_name + " WHERE age > 30"
print(query)

# Interview Questions on Concatenation
# Here are some questions you might encounter in interviews:

# Basic Questions

# What is string concatenation in Python?
# What are the different ways to concatenate strings in Python?
# How does list concatenation differ from tuple concatenation?

# Intermediate Questions

# What is the difference between using + and join() for string concatenation?
# Why is "".join(list_of_strings) preferred over + when concatenating multiple strings?
# What happens when you try to concatenate a string and an integer in Python?
# Advanced Questions

# How does concatenation impact performance, especially in a loop?
# How would you concatenate multiple large strings efficiently?
# Can you concatenate different data types? How?

# Coding Challenges

# Write a Python function that takes a list of names and returns a single string where 
# all names are concatenated with a comma.

names = ["Anshu", "Rahul", "Sneha", "Priya"]
print (names)


# Given two lists, concatenate them into a single list without using 
# the + operator.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print(merged_list)


# INPUT Function in Python input()
# In Python, the input() function is used to capture user input from 
# the console. 
# How It Works?
# When input() is called, the program pauses and waits for the user to
#  type something and press Enter. Whatever the user types is then 
# stored as a string.
# Example
name = input('What is your name: ')
print('Hello', name + "!" )

# By default, input() always returns a string, 
# even if the user types numbers. 
# So, we need to convert it if necessary: Example 1
age = input('What is your age : ')
print("My current Age is ", age)

# Example 2
age = int(input('What is your age : ')) # Convert string to integer
print("Next Year your Age : ", age + 1)


# Example 3
def add_numbers(a, b):
    return a + b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Sum:", add_numbers(x, y))


#  VARIABLES
# Variable is a concept in programming that allows us to give a 
# lable to a piece of data so that we can refer or referance 
# that data using the chosen variable name.
# A variable in Python is like a container that stores data. 
# Imagine it as a label you stick onto a box—whatever is inside 
# the box can be changed, but the label helps you refer to it.
# For example, if you want to remember someone's name in a program, 
# you can use a variable
name = "Anshu"
print(name)  # Output: Anshu

# Here, name is the variable, and "Anshu" is the value stored in it.

# Key Features of Variables in Python
# No Need to Declare Data Type
# Python automatically figures out what type of data is being stored.
age = 25        # Integer
price = 19.99   # Float
is_devops = True  # Boolean
# Can Change Values Anytime
x = 10
print(x)  # 10

x = "Hello"
print(x)  # "Hello"

# Dynamic Typing
# A variable's data type can change during execution.
# Case-Sensitive
# Age and age are different variables!


# Interview Questions on Variables in Python
# Basic Level Questions
# 1️ What is a variable in Python?
# 📌 A variable is a container that stores data.

# 2️⃣ How do you declare a variable in Python?
# 📌 Simply assign a value: x = 10

# 3️⃣ Does Python require variable type declaration?
# 📌 No, Python uses dynamic typing.

# 4️⃣ Is Python case-sensitive with variables?
# 📌 Yes, myVar and myvar are different variables.
# 5️⃣ How can you swap two variables without using a third variable?
# 📌 Using Python’s tuple unpacking feature:
a, b = 5, 10
a, b = b, a
print(a, b)  # Output: 10 5

# Advanced Level Questions
# 6️⃣ What happens when you assign one variable to another?
x = 10
y = x
y = 20
print(x)  # ???
# 📌 x remains 10 because integers are immutable.

# What are global and local variables?
# 📌 Local variables exist inside functions, global ones exist 
# throughout the program
global_var = "I am global"

def my_func():
    local_var = "I am local"
    print(local_var)

my_func()
print(global_var)

# How can you define a constant in Python?
# 📌 Python doesn’t have built-in constants, but by convention, 
# uppercase names are used:
MAX_USERS = 100

# What is variable shadowing in Python?
# 📌 When a local variable in a function has the same name as a
# global variable, the local variable takes precedence inside the
#  function.

# 10️⃣ What is the difference between mutable and immutable variables?
# 📌 Mutable variables (like lists) can be changed, immutable ones
#  (like strings and tuples) cannot be modified after creation.

my_list = [1, 2, 3]
my_list.append(4)  # ✅ Allowed (Mutable)

my_string = "Hello"
my_string[0] = "Y"  # ❌ Error (Immutable)


# len() Function in Python 
# The len() function in Python is like a quick counter—it tells you
# how many items are in a list, string, tuple, dictionary, or other 
# iterable data structures.

# Think of it as checking the length of a queue at a store. 
# If 5 people are standing in line, len(queue) would return 5.

# How It Works?
# The len() function is built-in, meaning you don’t need to import 
# anything—just use it directly.

name = "Anshu"
print(len(name))  # Output: 5
# Here, Python counts the number of characters 
# in "Anshu" and returns 5.

# Real-Time Use Cases of len()

# Development Scenarios
# 📌 Validating User Input in Web or CLI Apps

# When a user signs up, you might want to check if their password is
# at least 8 characters long.

password = input("Enter your password: ")
if len(password) < 8:
    print("Password too short! Must be at least 8 characters.")

    # Processing Lists of Data in Automation Scripts

# Suppose you are working with a list of filenames and
#  need to check how many files exist.
files = ["file1.txt", "file2.txt", "file3.txt"]
print("Total files:", len(files))  # Output: 3

# Limiting Text Length in a Chat App

# If you're building a chat system, limit message length to avoid spam.

message = input("Enter your message: ")
if len(message) > 200:
    print("Message too long! Please keep it under 200 characters.")


#Project 1 (Create Band Name usinfg all the concept you leearn above)

print ("Welcome to the Band Name Genetator App")
city = input ('Enter the name of city you belongs to: \n')
pet_name = ('Enter your pet name: \n ')
print ('Your Band Name is '+ city + " "+ pet_name)

