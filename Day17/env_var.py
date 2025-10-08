# This program demonstrates how to read an environment variable in Python.
import os
# Get the value of the environment variable 'password'
print (os.getenv('password'))
print (os.getenv('user')) # Another way to get the value of the environment variable 'user'