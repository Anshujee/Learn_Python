Python Variables and Scope – Learning Guide
This guide introduces the fundamental concepts of variables, typing, scope, and real-world DevOps scenarios in Python. It provides annotated examples and demonstrations for beginners and practitioners.

🧠 Topics Covered
Python Variables (Basics)

Dynamic Typing

Multiple Assignments

Type Casting

Getting Variable Types

Variable Scope (Local vs Global)

DevOps Use-Cases

📌 Python Variables
Variables are names assigned to values. They let you store, reuse, and manipulate data.

python
x = 5
name = "Anshu"
print(x)
print(name)
🔁 Dynamic Typing
Python is dynamically typed—you can reassign different data types to the same variable.

python
x = 10
x = "Now a string"
print(x)
🧮 Multiple Assignments
Assign the same or different values to multiple variables concisely.

python
a = b = c = 240588
print(a, b, c)

x, y, z = 1, 2.5, "Anshu"
print(x, y, z)
🔄 Type Casting
Convert data types using built-in functions: int(), float(), str(), etc.

python
x = "24"
print(type(x))  # string

print(float("25"))  # 25.0
print(float(400))   # 400.0
print(str(35))      # '35'
🔍 Getting Variable Types
Use type() to inspect the data type of any value.

python
n = 42
f = 3.14
s = "Hello"
li = [1, 2, 3]
d = {"key": "value"}
b = True

print(type(n), type(f), type(s), type(li), type(d), type(b))
🌍 Global vs Local Scope
Global Variable
Accessible throughout the script—even inside functions.

python
x = "Anshu"

def function():
    print("Inside:", x)

function()
print("Outside:", x)
Local Variable
Defined and accessible only within a function.

python
def function():
    x = "Local"
    print(x)

function()
# print(x)  # Would cause error
📌 nonlocal Keyword Example
python
def outer():
    x = "hello"
    def inner():
        nonlocal x
        x = "world"
    inner()
    return x

print(outer())  # world
🛠 Real-World DevOps Example: EC2 Instance Creation
Using Global and Local Variables
python
aws_region = "us-east-1"

def create_ec2_instance():
    instance_type = "t2.micro"
    print(f"Creating Instance in {aws_region} of type {instance_type}")

create_ec2_instance()
Using Return Values
python
def ec2_instance():
    return "t2.micro"

instance_type = ec2_instance()
print(f"Creating Instance in {aws_region} of type {instance_type}")
🚀 DevOps Use-Case with Environment Types
python
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
✅ Summary
This guide introduces:

Dynamic typing in Python

Variable scopes and visibility

Real-world use cases like EC2 automation

It serves as a solid foundation for Python learners and DevOps engineers using Python scripts for infrastructure automation.