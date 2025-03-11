# DATA TYPES IN PYTHON
# Data types are the foundation of Python programming.
# Whether you are developing applications or automating 
# infrastructure in DevOps, understanding data types helps 
# you write efficient, bug-free code.

# Imagine Python as a smart organizer that keeps different types of data
# in different boxes based on what they are.

# Python automatically detects and assigns the right box (data type) 
# when you create a variable.

user_name = "Anshu"
user_age = 30
user_salary = 85000.50
print(f"User {user_name} is {user_age} years old and earns {user_salary}.")

# Types of Data in Python

# Numeric Data Type :
# 1️⃣ Numbers (int, float, complex)
# These are used to store numerical values.

# 🔹 Integer (int): Whole numbers (positive, negative, or zero).
age = 30
year = 2025
print (age, year)

# 🔹 Floating-point (float): Numbers with decimals.
price = 99.99
pi = 3.14159
print (price,pi)
# 🔹 Complex (complex): Numbers with a real and imaginary part.
z = 2 + 3j
print(z)

# Real-world Use Cases:
# ✔ Handling user age, salaries, number of items in a cart (integers).
# ✔ Working with prices, discounts, and scientific calculations (floats).
# ✔ Used in machine learning and simulations (complex numbers).


# Sequence Data Type : (String, List, Tuple)
# 2️⃣ Strings (str) - Text Data
# A string is just a sequence of characters (letters, numbers, symbols).
# Strings must be enclosed in quotes.
name = "Anshu"
message = 'Hello, Python!'
print (name, message)

# 📌 Real-world Use Cases:
# ✔ Storing usernames, emails, messages, and logs.
# ✔ Handling API responses and file paths.
# Example - 
file_path = "/home/user/data.txt"
api_response = '{"status": "success"}'
# print(file_path, api_response)


# 4️⃣ Lists (list) - Ordered Collection
# A list is a collection of multiple values that can be modified.
servers = ["AWS", "Azure", "GCP"]
numbers = [1, 2, 3, 4, 5]
print (servers,numbers)
# ✅ Lists allow duplicate values and different data types.
mixed_list = ["Anshu", 30, True, 5.5]
print(mixed_list)
# Real-world Use Cases:
# ✔ Storing cloud instances in DevOps.
# ✔ Processing log files and API responses.
server_list = ["server1", "server2", "server3"]
print(f"Total active servers: {len(server_list)}")

# 5️⃣ Tuples (tuple) - Immutable Ordered Collection
# A tuple is just like a list, but unchangeable (immutable).
coordinates = (18.52, 73.85)  # Latitude and longitude
colors = ("red", "green", "blue")
print (coordinates,colors)

# Real-world Use Cases:
# ✔ Storing fixed data like GPS coordinates, months of the year.
# ✔ Performance optimization - tuples are faster than lists.

#  Boolean Data Type : (True or False)
# 3️⃣ Boolean (bool) - True or False
# Booleans represent only two values: True or False.
# Real-world Use Cases:
# ✔ Checking login authentication (is_authenticated = True).
# ✔ Feature flagging in software development (feature_enabled = False).

# Mapping Data Type : dictionary 
# 6️⃣ Dictionary (dict) - Key-Value Pairs
# A dictionary stores data in key: value pairs.
user = {"name": "Anshu", "role": "DevOps Engineer", "location": "Pune"}
print (user)
# In the above example Keys are name, roles, location and 
# values are Anshu, DevOps Engineer, Pune
# 
# ✅ Keys must be unique, values can be any data type.

config = {"timeout": 30, "retry": True, "api_key": "XYZ123"}
print (config)
# 📌 Real-world Use Cases:
# ✔ Storing configuration settings in DevOps.
# ✔ Processing JSON data from APIs.

# Set Data Types: (Set and Forzen Set)
# 7️⃣ Sets (set) - Unordered Unique Collection
# A set is like a list, but stores only unique values.
unique_ips = {"192.168.1.1", "192.168.1.2", "192.168.1.3"}
print (unique_ips)

# Binary Data Types: (bytes and bytearray)

# bytes: Represents immutable sequences of bytes. Example: data = b'Hello'
# bytearray: Represents mutable sequences of bytes. Example: data = bytearray(b'Hello')

# None Data Type:

# NoneType: Represents the None object, which is used to indicate the absence of a value or a null value.

# Custom Data Types:

# You can also define your custom data types using classes and objects.

# Python Core Questions

# 1️⃣ What are Python's built-in data types?
# Python provides several built-in data types, including:

# Numeric Types: int, float, complex
# Sequence Types: list, tuple, range
# Text Type: str
# Set Types: set, frozenset
# Mapping Type: dict
# Boolean Type: bool
# Binary Types: bytes, bytearray, memoryview
# None Type: NoneType
# How do you check the type of a variable in Python?
x = 10
print(type(x))  # Output: <class 'int'>

# 5️⃣ What is the difference between is and == in Python?

# ==	Compares values (checks if values are equal)
# is	Compares memory addresses (checks if objects are the same instance

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True (values are same)
print(a is b)  # False (different memory locations)

# Real-time Example in DevOps:

# ==: Comparing file contents (file1_contents == file2_contents).
# is: Checking if two objects point to the same log stream instance (log_stream1 is log_stream2).

# DevOps Python Questions
# 6️⃣ How are Python dictionaries used in DevOps automation?

# 📌 Real-time IT Scenario:
# Python dictionaries (dict) store key-value pairs and are 
# widely used in DevOps automation, such as:
# Managing AWS EC2 Instances
ec2_instances = {
    "instance_1": {"id": "i-12345", "state": "running"},
    "instance_2": {"id": "i-67890", "state": "stopped"},
}
print(ec2_instances["instance_1"]["state"])  # Output: running

# 7️⃣ What data types are best for handling infrastructure configurations?

# Dictionaries (dict) → Store key-value infrastructure details.
# Lists (list) → Store multiple configurations (e.g., list of IPs).
# JSON (json) → Store structured configuration data in cloud APIs.
# 📌 Example: Managing AWS EC2 instances in JSON format.
import json

config_data = {
    "Region": "us-east-1",
    "InstanceType": "t2.micro",
    "SecurityGroups": ["sg-12345", "sg-67890"]
}

print(json.dumps(config_data, indent=4))  # Pretty-printed JSON

# 8️⃣ How would you handle a list of log file paths in Python?

# 📌 Scenario: Automating log analysis from multiple servers.

log_files = ["/var/log/syslog", "/var/log/nginx/access.log", "/var/log/nginx/error.log"]

for log in log_files:
    with open(log, "r") as f:
        print(f"Reading {log}...")
        print(f.readlines()[:5])  # Print first 5 lines
# Used in log rotation, log aggregation, and log parsing.

# 9️⃣ What is the best way to remove duplicates 
# from a log file in Python?

# 📌 Scenario: A log file contains duplicate entries due 
# to repeated cron job execution.

# Solution: Use a set to remove duplicates.
log_file = "server_logs.txt"

with open(log_file, "r") as f:
    unique_logs = set(f.readlines())  # Remove duplicates

with open("cleaned_logs.txt", "w") as f:
    f.writelines(unique_logs)  # Write back unique logs

# Advantage: Faster and memory-efficient than looping over logs manually.

# 🔟 How do you validate JSON data types in an API response 
# using Python?
# Scenario: Validating an API response from a cloud service 
# (e.g., AWS, Azure).

# Solution: Use the jsonschema library.

import json
from jsonschema import validate, ValidationError

# Expected JSON Schema
schema = {
    "type": "object",
    "properties": {
        "instance_id": {"type": "string"},
        "status": {"type": "string"},
        "cpu_usage": {"type": "number"}
    },
    "required": ["instance_id", "status", "cpu_usage"]
}

# Sample API Response
api_response = '''{
    "instance_id": "i-12345",
    "status": "running",
    "cpu_usage": 75.5
}'''

# Convert JSON string to dictionary
data = json.loads(api_response)

# Validate JSON
try:
    validate(instance=data, schema=schema)
    print("JSON is valid")
except ValidationError as e:
    print("JSON validation failed:", e)

# Real-time IT Case Scenario:

# Validating AWS/Azure API responses before automation scripts execute 
# actions.
# Ensuring compliance with expected infrastructure configurations.




