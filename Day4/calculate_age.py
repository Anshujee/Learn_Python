# Ask for the user's name
name = input ("what is your Name ?")
# Ask for the birth year and convert it to an integer
birth_year = int(input(" What is your Year of Birth ?"))
# Calculate the age (assuming the current year is 2025)
current_year = 2025

age = current_year - birth_year
# Print a personalized message with age
print ( "Hello ! " + name + "you are "+ str(age) + " years old.")
