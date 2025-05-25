a = int(input("Enter first number : "))
b = int(input("Enter second Number : "))
operator = int(input( 'pleae enter 1 for add , 2 for subtract or 3 for Multiplication  operation : '))
if operator == 1:
    print("Result :" , a+b)
elif operator == 2:
    print ("Result :", a-b)
elif operator == 3:
    z = a * b 
    print (" Result :", a*b)
else:
    print ("Invalid Operation")