

#Loops
#For
x = []

for i in range(10):
	x.append(i)
	print(x)

for i in x:
	print("The index is %d" % x[i])

ages = {"Eli":26,  "Heather":22}

for name, age in ages.items():
	print("%s is %d years old" % (name,age))

#While

n = 0
while n < 10:
	print(n)
	n += 1