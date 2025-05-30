from __future__ import print_function
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()

######################################################################
fruits = ["apple", "orange", "kiwi"]

for fruit in fruits:

    print(fruit)

#########################################################################

for i in range(int(2.0)):
   print(i)

######################################################################### 

x = 'abcd'
for i in range(len(x)):  
    print(i, end= "")

######################################################################
d = 1
while True :
    if d % 7 == 0:
        break
    print (d, end= " ")
    d += 1


###################################################################
T = int (input ( "Enter a number : - "))
for t in range (1 , 11):
    print (t * i, end= " ")