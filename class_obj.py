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