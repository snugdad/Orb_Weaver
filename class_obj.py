#######################################
"""
Intro to Classes:
"""
#######################################

class Animal(object):
    name = ""

    def eat(self):
        print("%s is eating..." % self.name)
    def sleep(self):
        print("%s is sleeping..." % self.name)

class Mammal(Animal):
    hasBackBone = True
    hasHair = True

    def growHair(self):
        print("Growing hair")

cat = Mammal()
dog = Mammal()
cat.name = "Shakes"
dog.name = "Holly"

cat.eat()
dog.sleep()

class MyClass:
    """ A simple example class """
    i = 12345
    counter = 0;
    def f(self):
        return 'hello world'

x = MyClass()
counter = 1
while x.counter < 10:
    x.counter += 1
print(x.counter)
del x.counter

myList = ["hello", "world"]

print(myList)