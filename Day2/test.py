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

# 3️⃣ Boolean (bool) - True or False
# Booleans represent only two values: True or False.
# Real-world Use Cases:
# ✔ Checking login authentication (is_authenticated = True).
# ✔ Feature flagging in software development (feature_enabled = False).


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

# 7️⃣ Sets (set) - Unordered Unique Collection
# A set is like a list, but stores only unique values.
unique_ips = {"192.168.1.1", "192.168.1.2", "192.168.1.3"}
print (unique_ips)

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
