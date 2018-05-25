

def doSomething():
    print("Hello World")

def getList(max):
    x = list(range(max))
    for i in x:
        x[i] = i * 5
    return x

def getPerson(name = "Unknown", age=0):
    print("The person's name is %s" % name)
    print("They are %d years old" % age)
doSomething()
myList = getList(200)
print(myList)
getPerson("Eli", 26)

h = 2
if h > 4:
    getPerson("Eli", 26)
else:
    getPerson("Heather", 22)