# Inbuilt Functions in Python

## Definition:

Inbuilt functions in Python are **pre-defined functions** available in the Python Standard Library. These functions are always available for use **without the need for any additional imports or installations**. They provide a wide range of functionalities, from mathematical operations to data type conversions, making it easier for developers to perform common tasks efficiently.

## Why Use Inbuilt Functions?

* **Efficiency**: Optimized for performance.
* **Reusability**: Eliminates the need to write repetitive code.
* **Readability**: Makes code easier to understand and maintain.
* **Reduced Errors**: Built-in and well-tested functions are less prone to errors.

Inbuilt functions simplify and speed up the development process. For **DevOps engineers**, they are particularly useful for automating tasks, processing data, and managing system operations.

---

## List of Common Python Inbuilt Functions

### 1. Input/Output Functions

| Function  | Description                 |
| --------- | --------------------------- |
| `print()` | Outputs data to the console |
| `input()` | Takes user input            |

**Example:**

```python
# Print function
print("Hello, DevOps Engineers!")

# Input function
user_name = input("Enter your name: ")
print(f"Welcome, {user_name}!")
```

---

### 2. Type Conversion Functions

| Function  | Description                         |
| --------- | ----------------------------------- |
| `int()`   | Converts to an integer              |
| `float()` | Converts to a floating-point number |
| `str()`   | Converts to a string                |
| `bool()`  | Converts to a boolean               |

**Example:**

```python
num_str = "100"
num_int = int(num_str)
num_float = float(num_int)

print(type(num_str), type(num_int), type(num_float))
# Output: <class 'str'> <class 'int'> <class 'float'>
```

---

### 3. Mathematical Functions

| Function    | Description                         |
| ----------- | ----------------------------------- |
| `abs()`     | Returns the absolute value          |
| `pow(x, y)` | Returns x raised to power y         |
| `round()`   | Rounds a number to y decimal places |
| `min()`     | Returns the smallest value          |
| `max()`     | Returns the largest value           |
| `sum()`     | Returns the sum of all items        |

**Example:**

```python
print(abs(-10))             # 10
print(pow(2, 3))            # 8
print(round(3.14159, 2))    # 3.14
print(min(10, 5, 20))       # 5
print(max(10, 5, 20))       # 20
print(sum([1, 2, 3, 4, 5])) # 15
```

---

### 4. String Functions

| Function    | Description                     |
| ----------- | ------------------------------- |
| `len()`     | Returns the length of a string  |
| `lower()`   | Converts to lowercase           |
| `upper()`   | Converts to uppercase           |
| `strip()`   | Removes leading/trailing spaces |
| `replace()` | Replaces a substring            |
| `split()`   | Splits a string into a list     |

**Example:**

```python
text = " DevOps Automation "
print(len(text))                    # 21
print(text.lower())                # " devops automation "
print(text.upper())                # " DEVOPS AUTOMATION "
print(text.strip())                # "DevOps Automation"
print(text.replace("DevOps", "Cloud")) # " Cloud Automation "
print(text.split())                # ['DevOps', 'Automation']
```

---

### 5. List Functions

| Function    | Description                     |
| ----------- | ------------------------------- |
| `len()`     | Returns number of items in list |
| `append()`  | Adds an element to end of list  |
| `pop()`     | Removes and returns last item   |
| `sort()`    | Sorts the list                  |
| `reverse()` | Reverses the list               |

**Example:**

```python
tools = ["Terraform", "Ansible", "Docker", "Kubernetes"]
print(len(tools))  # 4
tools.append("Jenkins")
print(tools)
tools.pop()
print(tools)
tools.sort()
print(tools)
tools.reverse()
print(tools)
```

---

### 6. Dictionary Functions

| Function   | Description                 |
| ---------- | --------------------------- |
| `keys()`   | Returns a list of keys      |
| `values()` | Returns a list of values    |
| `items()`  | Returns key-value pairs     |
| `get()`    | Retrieves a value for a key |
| `pop()`    | Removes a key-value pair    |

**Example:**

```python
devops_tools = {"CI/CD": "Jenkins", "Containerization": "Docker", "Orchestration": "Kubernetes"}

print(devops_tools.keys())
print(devops_tools.values())
print(devops_tools.get("CI/CD"))
devops_tools.pop("CI/CD")
print(devops_tools)
```

---

## Real-Time Example in DevOps Engineering

### Scenario: Automating Cloud Cost Optimization

A DevOps engineer wants to monitor and optimize AWS costs by checking the running EC2 instances and filtering out unused instances using Python inbuilt functions.

**Example Code:**

```python
import boto3

# Initialize AWS EC2 client
ec2_client = boto3.client("ec2")

# Fetch running instances
instances = ec2_client.describe_instances()

# Extract instance IDs
instance_ids = [instance["InstanceId"] for res in instances["Reservations"] for instance in res["Instances"]]

# Print instance count using len()
print(f"Total Running Instances: {len(instance_ids)}")

# Using min() to find the smallest instance ID (example purpose only)
if instance_ids:
    print(f"Smallest Instance ID: {min(instance_ids)}")
else:
    print("No instances found!")
```

### Explanation:

* `boto3.client("ec2")`: Creates an EC2 client.
* `describe_instances()`: Fetches running EC2 instances.
* `len(instance_ids)`: Counts the number of running instances.
* `min(instance_ids)`: Finds the smallest instance ID.

---

## Conclusion

* Python inbuilt functions **simplify tasks** by providing ready-made solutions.
* They are **widely used in DevOps** automation, cloud operations, and infrastructure management.
* Using functions like `len()`, `min()`, `max()`, and `sum()` **enhances script efficiency** and reduces code complexity.

---

**Happy Learning & Automating!**

> *"Write less, automate more — with Python's inbuilt power."*
