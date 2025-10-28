import calc as advance

#advance.add()
#advance.subtract()

#print ("Addition from advanced calc :", advance.add())
#print ( " Sub from advanced calc :", advance.subtract())
# Here we have imported calc module and used its functions.
# Now we want to import only add function from calc module.
# For that we can use from keyword.
from calc import add
print ("Addition from advanced calc using from keyword :", add())
# Here we have imported only add function from calc module.