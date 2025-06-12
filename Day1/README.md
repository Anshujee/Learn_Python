                                           “Basics of Python”
# 🐍 Python Basics for Beginners

Welcome to this beginner-friendly guide where we explore the foundational concepts of **Python programming**, from simple print statements to basic user input, variables, string/list/tuple concatenation, and more — including a mini project at the end!

---

## 📘 Table of Contents

- [🔹 Print Statements](#-print-statements)
- [🔹 String Concatenation](#-string-concatenation)
- [🔹 List & Tuple Concatenation](#-list--tuple-concatenation)
- [🔹 input() Function](#-input-function)
- [🔹 Variables in Python](#-variables-in-python)
- [🔹 len() Function](#-len-function)
- [🔹 Mini Project: Band Name Generator](#-mini-project-band-name-generator)
- [🧠 Interview Questions](#-interview-questions)

---

## 🔹 Print Statements

```python
print("Hello World!")   # Double quotes
print('Hello Anshu')    # Single quotes

print('I am starting to learn Python\nHello Anshu')
print("Hi\nI am Anshu\nI am learning Python\nIt is very good to upskill.")


🔹 String Concatenation
Concatenation joins strings using + or .join().
# Using +
print('Hello' + ' Anshu')
first_name = "Anshu"
last_name = "Jee"
full_name = first_name + " " + last_name
print(full_name)

# Using join()
words = ["Hello", "world", "!"]
sentence = " ".join(words)
print(sentence)

🔹 List & Tuple Concatenation
# List Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print(merged_list)

# Tuple Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print(merged_tuple)

🔹 input() Function
Captures user input from the terminal.

name = input('What is your name: ')
print('Hello', name + "!")

age = int(input('What is your age: '))
print("Next year, your age will be:", age + 1)

🔹 Variables in Python
Variables are labels used to store data.
name = "Anshu"
age = 25
price = 19.99
is_devops = True

# Dynamic typing
x = 10
x = "Hello"

# Swapping
a, b = 5, 10
a, b = b, a
print(a, b)  # Output: 10 5

🔹 len() Function
Gives the number of items in a string, list, tuple, etc.

name = "Anshu"
print(len(name))  # Output: 5

files = ["file1.txt", "file2.txt", "file3.txt"]
print("Total files:", len(files))  # Output: 3

password = input("Enter your password: ")
if len(password) < 8:
    print("Password too short!")

message = input("Enter your message: ")
if len(message) > 200:
    print("Message too long!")

🧠 Interview Questions
📌 String Concatenation
What is string concatenation in Python?

What are the different ways to concatenate strings?

Difference between + and .join()?

📌 Variables
What is a variable in Python?

Does Python require data type declaration?

How can you swap two variables?

What are global vs local variables?

What are mutable vs immutable variables?

🙌 Conclusion
This guide covers the essential building blocks of Python. Practice these concepts regularly to build a strong foundation.