'''
Inheritance property
reuse properties/methods from a parent class
parent class
p1 p2

child class
p3 p4

'''
class animal:
    def speak(self):
        print('Animals make sounds')

class dog(animal):
    def bark(self):
        print('Dogs bark')

dog = Dog()
dog.speak()
dog.bark()

