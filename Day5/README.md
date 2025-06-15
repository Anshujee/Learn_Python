# 🐍 Python Variables – Beginner to Pro with Real-World DevOps Examples

This document explains Python variables from basic to advanced level with real-world DevOps scenarios.

---

## 📌 What are Python Variables?

In Python, variables are used to store data that can be referenced and manipulated during program execution. A variable is essentially a name assigned to a value.

> ✅ Variables act as placeholders for data and allow us to store and reuse values in our program.

### Example:
```python
x = 5
name = "Anshu"
print(x)
print(name)
⚙️ Dynamic Typing in Python
Python is dynamically typed, meaning:

You don't need to declare the type explicitly.

The same variable can hold values of different types.

python
Copy
Edit
x = 10
x = "Now a string"
print(x)
🧮 Multiple Assignments
1. Assigning the same value:
python
Copy
Edit
a = b = c = 240588
print(a, b, c)
2. Assigning different values:
python
Copy
Edit
x, y, z = 1, 2.5, "Anshu"
print(x, y, z)
🔁 Type Casting (Changing Data Types)
Convert values from one data type to another using int(), float(), str() etc.

python
Copy
Edit
x = "24"
print(type(x))  # str
y = "25"
print(float(y))  # 25.0
y = 400
print(float(y))  # 400.0

age = 35
print(str(age))  # "35"
z = str(age)
a = float(z)
print(a)  # 35.0
🔍 Checking Variable Type
Use the built-in type() function to check the data type of a variable.

python
Copy
Edit
n = 42
f = 3.14
s = "Hello, World!"
li = [1, 2, 3]
d = {'key': 'value'}
bool = True

print(type(n))   # <class 'int'>
print(type(f))   # <class 'float'>
print(type(s))   # <class 'str'>
print(type(li))  # <class 'list'>
print(type(d))   # <class 'dict'>
print(type(bool))# <class 'bool'>
🌐 Scope of Variables
Python variables have two types of scope:

1. Global Variables
Defined outside of functions and accessible throughout the program.

python
Copy
Edit
x = "Anshu"

def function():
    print("Print Inside Function:", x)

function()
print("Print Outside Function:", x)
2. Local Variables
Defined inside a function and can only be used within that function.

python
Copy
Edit
def function():
    x = "Anshu"
    y = "I am learning Python"
    print(x)
    print(y)

function()
❌ Trying to access a local variable outside its function causes an error:
python
Copy
Edit
def f():
    h = "Ayan Verma"

f()
print(h)  # NameError: name 'h' is not defined
🚀 Real DevOps Example – AWS EC2 Script
Global and Local Variables
python
Copy
Edit
aws_region = "us-east-1"  # Global variable

def create_ec2_instance():
    instance_type = "t2.micro"  # Local variable
    print(f"Creating Instance in {aws_region} of type {instance_type}")

create_ec2_instance()
Alternate Version Using Return
python
Copy
Edit
def ec2_instance():
    return "t2.micro"

instance_type = ec2_instance()
print(f"Creating Instance in {aws_region} of type {instance_type}")
🧪 Local vs Global Example
python
Copy
Edit
x = 10

def test():
    x = 20
    print(x)  # 20

test()
print(x)  # 10
🔄 Using nonlocal for Nested Functions
python
Copy
Edit
def outer():
    x = "hello"
    def inner():
        nonlocal x
        x = "world"
    inner()
    return x

print(outer())  # Output: world
✅ Real DevOps Use-Case Scenario
You're automating EC2 instance creation using Boto3. You select the instance type based on environment (dev, test, prod).

python
Copy
Edit
aws_region = "us-east-1"

def create_instance(env):
    if env == "dev":
        instance_type = "t2.large"
    elif env == "test":
        instance_type = "t2.mini"
    elif env == "pro":
        instance_type = "t2.Xlarge"
    else:
        instance_type = "t2.micro"
    
    print(f"Creating EC2 instance in {aws_region} with instance type {instance_type}")

create_instance("dev")
create_instance("test")
create_instance("pro")
📘 Summary
Concept	Description
Variable	Symbolic name assigned to a value
Dynamic Typing	Type of variable decided at runtime
Multiple Assignment	Assign multiple variables in one line
Type Casting	Convert data from one type to another
type()	Function to check the variable’s type
Global Scope	Accessible everywhere
Local Scope	Accessible only inside the defining function
DevOps Example	Automate AWS EC2 instance creation using local & global variables in Python

✨ Keep practicing and applying these concepts to your DevOps automation scripts for real-world mastery!

yaml
Copy
Edit

---

Let me know if you’d like:
- A downloadable `.md` or `.pdf` file
- An illustrative mind map
- Sample GitHub `repo` structure for uploading this content.