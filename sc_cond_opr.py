#Scope, Conditions, Operations

########################################
# Conditions
"""
JAVA

scope 0
    if()
        scope 1
        if()
            scope 5
    if()
        scope 4
scope 3
"""
########################################

x = 9
if x == 9:
    print("9 is here")

x = 8
if x != 9:
	print("9 is no more")

x = 11
if x > 10:
	print("greater than 10")
else:
	print("less than 10")
########################################
#Boolean
"""
	BOOLEAN
"""
########################################

name = "Eli"
age  = 26
array = ["dog", "cat", "bird", "elephant"]

if age > 26:
	print ("NOT POSSIBLE")
else:
	print ("TRUE")

if "bird" in array:
	print("WOOOW A BIRDIE")
if "elephant" in array:
	print("OOOOO AN ELEEPHAAAANT")
if "cat" in array:
	print("KITTY")
else:
	print("oooooonoooooooooaoaooaaa")


#Comparison

a = (1,2,3,4,5)
b = (1,2,3,4,5)

if a == b:
 	print("They are the same")
else:
	print("They are not the same")
if a is b:
	print("They are the same object")
else:
	print("They are not the same object")

# Nested If statements
name = "Eli"
age = 26
pet = "cat"

if name == "Eli":
	print("Hello %s" % name)
	if age == 26:
		print("You're %d, arent you?" % age)
else:
	print("IDK YOUUUUU")
