import re

##################################################
"""
	String Manipulation: 
				Object Oriented Approach
"""
##################################################

str = "Hello World"

#Print strlen
print("String is %d bytes long" % len(str))

#Make uppercase
print(str.upper())

#Make lowercase
print(str.lower())

#find index of a letter
print("The position of the first o is: %d\n" % str.index('o'))

#Count number of l's 
print("There are %d letter L's in %s" % (str.upper().count("L"), str))

#Slice the string
print(str[3])
print(str[1:6])
print(str[1:len(str)])

##################################################
"""
	Lists:
			Lists are RDWR data types similiar to
			arrays, they can have any sort of data
			type within them
"""
##################################################

name = "Elias Goodale"
print(str.split(" "))
mylist = name.split(" ")
print(mylist)
print("My first name is %s and my last name is %s" % (mylist[0], mylist[1]))

mList = [1,2,3,4,5,"dog","cat","bird"]
print (mList)

#count the number of cats
print("There are %d cat(s)" % mList.count("cat"))

#count the number of objects in the list 
print("There are %d number of objects in the list" % len(mList))

#print the cats position in the list
print("The cat is at position: %d" % mList.index("cat"))

#insert into the list
mList.insert(2, "fish")
print (mList)

#append to the list
mList.append("snake")
print(mList)

#remove an item from the list
mList.remove("fish")
print(mList)

#reverse the list
mList.reverse()
print(mList)


#sort the numeric part of the list only
newList = mList.copy()
newList.reverse()
newList = newList[0:5]
newList.sort()
print(newList)

#modify an item in the list
newList[0] = "LOL"
print(newList)

###################################################

"""
Tuples:
		Tuples are fixed sized, immutable data types,
		Tuples are read only data types,
		Tuples, once instantiated cannot be written
"""
###################################################
myTuple = (1, 2, 3, 4, 5, 'Tuple')
print(myTuple)

print("The index of 3 is %d" % myTuple.index(3))

###################################################
"""
Dictionaries:
			key value list pairs that are accessed
			via the keys(item name), values
			(item value), and items(both)

"""
###################################################

ages = {"Bryan":40, "Heather":22}
print(ages)

print(ages.keys())
print(ages.values())
print(ages.items())

print(ages["Bryan"])

del ages["Bryan"] # can use pop, pop, however returns the value
print(ages)

#Add an item in
ages["Bryan"] = 40
print(ages.items())

#Modify a value
ages["Bryan"] = 99 #This is how you can modify the values in a tuple. this is because it is edited in memory
print (ages)

if "Heather" in ages.keys():
	print ("TRUE!")