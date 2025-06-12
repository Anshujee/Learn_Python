# Python Data Types for DevOps Engineers

A data type in Python is a category that defines what kind of value a variable can hold. Think of data types as labels that tell Python how to treat different kinds of data. Python is dynamically typed, so you don’t need to declare the data type explicitly — Python figures it out based on the assigned value.

---

## 📊 Core Data Types in Python

Python offers several built-in data types, grouped broadly into the following categories:

### 1. Numeric Types

* `int`: Whole numbers (e.g., 5, -42, 1000)
* `float`: Decimal numbers (e.g., 3.14, -0.5)
* `complex`: Complex numbers (e.g., 2 + 3j)

**Use Case in DevOps:**

* Used in metrics calculation (e.g., CPU usage, RAM utilization).

---

### 2. Sequence Types

* `str`: Text data (e.g., 'Hello World')
* `list`: Ordered, mutable collection (e.g., \[1, 'hello', 3.14])
* `tuple`: Ordered, immutable collection (e.g., (1, 2, 3))

**Use Cases:**

* Strings: Log parsing, file paths, dynamic outputs.
* Lists: Storing configurations, paths, file names.
* Tuples: Fixed data like GPS coordinates.

---

### 3. Mapping Type

* `dict`: Key-value pairs (e.g., {'name': 'Anshu', 'age': 30})

**Use Cases:**

* Manage environment variables, AWS credentials, or JSON data.

---

### 4. Set Types

* `set`: Unordered collection of unique items (e.g., {1, 2, 3})
* `frozenset`: Immutable set.

**Use Case:**

* Deduplication in logs or datasets.

---

### 5. Boolean Type

* `bool`: True or False values

**Use Case:**

* Conditional logic in scripts.

---

### 6. Binary Types

* `bytes`, `bytearray`, `memoryview`: Handle binary data

**Use Case:**

* File uploads, encryption, binary APIs.

---

### 7. None Type

* `None`: Represents absence of value.

**Use Case:**

* Check if variables or env values are missing.

---

## 🔍 Sample Code: Data Types in Action

```python
user_name = "Anshu"
user_age = 30
user_salary = 85000.50
print(f"User {user_name} is {user_age} years old and earns {user_salary}.")
```

### Numeric

```python
age = 30
year = 2025
price = 99.99
pi = 3.14159
z = 2 + 3j
```

### String

```python
name = "Anshu"
message = 'Hello, Python!'
file_path = "/home/user/data.txt"
api_response = '{"status": "success"}'
```

### List

```python
servers = ["AWS", "Azure", "GCP"]
mixed_list = ["Anshu", 30, True, 5.5]
server_list = ["server1", "server2", "server3"]
```

### Tuple

```python
coordinates = (18.52, 73.85)
colors = ("red", "green", "blue")
```

### Boolean

```python
is_authenticated = True
feature_enabled = False
```

### Dictionary

```python
user = {"name": "Anshu", "role": "DevOps Engineer", "location": "Pune"}
config = {"timeout": 30, "retry": True, "api_key": "XYZ123"}
```

### Set

```python
unique_ips = {"192.168.1.1", "192.168.1.2", "192.168.1.3"}
```

---

## 🎓 Python Interview Questions for DevOps Engineers

### 1. What are Python's built-in data types?

* Numeric: int, float, complex
* Sequence: list, tuple, range
* Text: str
* Set: set, frozenset
* Mapping: dict
* Boolean: bool
* Binary: bytes, bytearray, memoryview
* None: NoneType

### 2. How do you check the type of a variable in Python?

```python
x = 10
print(type(x))  # <class 'int'>
```

### 3. What is the difference between `is` and `==` in Python?

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True (same values)
print(a is b)  # False (different memory location)
```

### 4. How are Python dictionaries used in DevOps automation?

```python
ec2_instances = {
    "instance_1": {"id": "i-12345", "state": "running"},
    "instance_2": {"id": "i-67890", "state": "stopped"},
}
print(ec2_instances["instance_1"]["state"])
```

### 5. What data types are best for infrastructure configurations?

* `dict` for key-value pairs
* `list` for multiple values
* `json` for structured data

```python
import json
config_data = {
    "Region": "us-east-1",
    "InstanceType": "t2.micro",
    "SecurityGroups": ["sg-12345", "sg-67890"]
}
print(json.dumps(config_data, indent=4))
```

### 6. How would you handle a list of log file paths?

```python
log_files = ["/var/log/syslog", "/var/log/nginx/access.log"]
for log in log_files:
    with open(log, "r") as f:
        print(f"Reading {log}...\n", f.readlines()[:5])
```

### 7. Best way to remove duplicates from logs?

```python
log_file = "server_logs.txt"
with open(log_file, "r") as f:
    unique_logs = set(f.readlines())
with open("cleaned_logs.txt", "w") as f:
    f.writelines(unique_logs)
```

### 8. How to validate JSON using `jsonschema`?

```python
from jsonschema import validate, ValidationError
schema = {
    "type": "object",
    "properties": {
        "instance_id": {"type": "string"},
        "status": {"type": "string"},
        "cpu_usage": {"type": "number"}
    },
    "required": ["instance_id", "status", "cpu_usage"]
}
data = {
    "instance_id": "i-12345",
    "status": "running",
    "cpu_usage": 75.5
}
try:
    validate(instance=data, schema=schema)
    print("JSON is valid")
except ValidationError as e:
    print("Validation failed:", e)
```

---

## 🏠 Summary

* Python data types are crucial for writing clean, effective automation scripts.
* In DevOps, understanding how to apply these data types to real-world problems will make you a more efficient engineer.

# 🧠 Understanding `type()` Function in Python

## 📘 What is the `type()` Function?

Imagine you are organizing your fridge.  
You have milk, eggs, fruits, and vegetables.  
You want to know what type of item each one is.  

Similarly, in Python, the `type()` function helps you identify the **type of a variable or value**.

It tells what kind of data is stored in a variable — just like labels on food packages help you understand what you're eating!

---

## 🧾 Syntax

```python
type(object)

x = 10
print(type(x))  # Output: <class 'int'>

y = 3.14
print(type(y))  # Output: <class 'float'>

name = "Anshu"
print(type(name))  # Output: <class 'str'>

my_list = [1, 2, 3]
print(type(my_list))  # Output: <class 'list'>

my_tuple = (10, 20, 30)
print(type(my_tuple))  # Output: <class 'tuple'>

my_dict = {"name": "Anshu", "role": "DevOps"}
print(type(my_dict))  # Output: <class 'dict'>

status = True
print(type(status))  # Output: <class 'bool'>

