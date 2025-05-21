    ################## Python Data Types  ##################
# Data types in Python define the type of value a variable holds — 
# like whether it's a number, text, list, or something else. 
# Python is dynamically typed, so you don't need to declare data types explicitly.
# Python data types are classes and variables are instances (objects) of these classes. 
# The following are the standard or built-in data types in Python:
# 1.  Numeric - int, float, complex
# 2.  Sequence Type - string, list, tuple
# 3.  Mapping Type - dict
# 4.  Boolean - bool
# 5.  Set Type - set, frozenset
# 6.  Binary Types - bytes, bytearray, memoryview

#################### Discuss some important Data Type ##########################
# 2. Sequence Data Types in Python
# The sequence Data Type in Python is the ordered collection of similar or different Python data types. 
# Sequences allow storing of multiple values in an organized and efficient fashion
# There are several sequence data types of Python:

# Python String
# Python List
# Python Tuple

########################################################################
# String Data Type
# Python Strings are arrays of bytes representing Unicode characters. In Python, 
# there is no character data type Python, a character is a string of length one. 
# It is represented by str class.

# Strings in Python can be created using single quotes, double quotes or even 
# triple quotes. We can access individual characters of a String using index.

s = 'Welcome to the World of Python'
print(s)

# check data type 
print(type(s))

# access string with index
print(s[0])
print(s[1])
print(s[2])
print(s[-1])
print(s[-2])


###############################################################################
# List Data Type
# A list is an ordered, mutable (changeable) collection that allows duplicate elements.
# It is one of the most commonly used data types in Python.
# Lists are just like arrays, declared in other languages which is an ordered 
# collection of data. 
# It is very flexible as the items in a list do not need to be of the same type.
# Creating a List in Python

# Lists in Python can be created by just placing the sequence inside the square brackets[].
# Empty list
a = []

# list with int values
a = [1, 2, 3]
print(a)

# list with mixed int and string
b = ["Anshu", "Pune", "Infosys", 4, 5]
print(b)


##########################################################################
# Tuple Data Type
# Just like a list, a tuple is also an ordered collection of Python objects. 
# The only difference between a tuple and a list is that tuples are immutable. 
# Tuples cannot be modified after it is created.
# Creating a Tuple in Python

# In Python Data Types, tuples are created by placing a sequence of values 
# separated by a ‘comma’ with or without the use of parentheses for grouping 
# the data sequence. Tuples can contain any number of elements and of any datatype
#  (like strings, integers, lists, etc.).

empty_tuple = ()
numbers = (1, 2, 3, 4)
mixed = (1, "Anshu", True, 3.14)
nested = (1, [2, 3], (4, 5))

print (empty_tuple)
print (numbers)
print(mixed)
print (nested)


#######################################################################
# Why Use Tuples?
# To protect data from being modified

# Tuples use less memory and are faster than lists

# Ideal for fixed data sets like days of the week, coordinates, config settings

################################################################################

###################### Set Data Type in Python ##############################
# In Python Data Types, Set is an unordered collection of data types that is 
# iterable, mutable, and has no duplicate elements. The order of elements in 
# a set is undefined though it may consist of various elements.
my_set = {1, 2, 3}
print (my_set)
print(type(my_set))  # Output: <class 'set'>

# Why Use Sets?
# Automatically remove duplicates

# Perform mathematical set operations (union, intersection, difference)

# Efficient membership testing (very fast in operation)

# Clean up data (e.g., remove duplicate IPs or config items)

numbers1= {1, 2, 3, 4}
mixed1= {1, "Anshu", True, 3.14}
duplicates = {1, 2, 2, 3, 3, 3}
print (numbers1)
print (mixed1)
print(duplicates)  # Output: {1, 2, 3}
##############################################################################
#   Set Operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # Union: {1, 2, 3, 4, 5}
print(a & b)   # Intersection: {3}
print(a - b)   # Difference: {1, 2}
print(a ^ b)   # Symmetric Difference: {1, 2, 4, 5}

##################################################################

# Real-World DevOps Example
# Remove duplicate AWS regions in a config:
aws_regions = ["us-east-1", "us-west-1", "us-east-1", "eu-central-1"]
unique_regions = set(aws_regions)

print(f"Deploying to regions: {unique_regions}")

#####################################################################
# Compare IPs from two sources:


dev_ips = {"10.0.0.1", "10.0.0.2"}
prod_ips = {"10.0.0.2", "10.0.0.3"}

common_ips = dev_ips & prod_ips
print(f"IPs in both Dev and Prod: {common_ips}")

#######################################################################
##################### Dictionary Data Type ##########################
# A Dictionary is a collection of key-value pairs
# Dictionary holds a key: value pair. Key-value is provided in the dictionary 
# to make it more optimized. Each key-value pair in a Dictionary is separated by 
# a colon : , whereas each key is separated by a ‘comma’.

my_disc = { "name" : "Anshu" ,
           "Role" : "DevOps Engineer ",
             "Location" : "Pune", 
               "Company" : "Infosys"  }
print (my_disc)
print (my_disc["name"])
print (my_disc["Role"])
print (my_disc["Location"])
# Another Way to print 

print ("Seprate")
print (my_disc.get("name"))
print (my_disc.get("Role"))
print (my_disc.get("Location"))
print (my_disc.get("Company"))

#############################################################################
    ############## Real-World DevOps Examples ################
   
    # 1.  Store EC2 instance metadata

ec2_instance = {
    "id": "i-1234567890",
    "type": "t2.micro",
    "region": "us-east-1",
    "status": "running"
}

print (ec2_instance .get ("type"))
print (ec2_instance.get ("region"))

# 2. Track Docker container states
docker_status = {
    "nginx": "running",
    "redis": "stopped",
    "postgres": "running"
}

print (docker_status.get("nginx"))
print (docker_status.get ("redis"))

# 3. Map environment to config

env_config = {
    "dev": {"instance_type": "t2.micro", "count": 2},
    "prod": {"instance_type": "m5.large", "count": 5}
}

print (env_config)

# Example: Dictionary + Conditional Logic 
aws_resources = {
    "ec2": "Running",
    "rds": "stopped",
    "s3": "active"
}

if aws_resources.get("ec2") == "running":
    print("EC2 is up and running.")
else:
    print ("EC2 is not running .Please restart the Instance")


