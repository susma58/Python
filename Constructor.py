'''
___init___()

'''

class car:
    def set_details(self, brand, color):
        self.brand = brand
        self.color = color

#creating objects
car1 = car()
car1.set_details('Tesla', 'Red')
print(car1.brand)
print(car1.color)

# With constructor
class car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        
car1 = car('Tesla', 'Red') #using constructor values set automatically
print(car1.brand, car1.color)

'''
syntax:
class ClassName:
    def ___init___(self, parameters1, parameter2):
        self.property1 = parameter1
        self.property2 = parameter2
        
___init___() constructor
self.property:
'''

# practice another
class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

# creating objects
student1 = student('Rakesh', 100, 'A+')
student2 = student('Kalpesh', 120, 'B+')

print(student1.name, student1.age, student1.grade)
print(student2.name, student2.age, student2.grade)


'''
Types of constructors
1- default constructor (self)
2- parameterized constructor (self, name, age)
3- constructor with default values, (self, name = 'Unknown', age = 0)
'''
