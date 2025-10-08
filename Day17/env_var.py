# This program demonstrates how to read an environment variable in Python.
import os
# Get the value of the environment variable 'password'
print (os.getenv('password'))
print (os.getenv('user')) # Another way to get the value of the environment variable 'user'

# To Set the envvariable in terminal use the below command
# export password='your_password'
# export user='your_user'
# To run the program use the below command
# python3 env_var.py by importing os module
# To unset the envvariable in terminal use the below command
# unset password
# unset user
# To check the envvariable in terminal use the below command
# printenv | grep password
# printenv | grep user
# echo $password
# echo $user
# Note: The environment variable will be available only in the current terminal session.
#  If you open a new terminal, you will need to set the variable again.