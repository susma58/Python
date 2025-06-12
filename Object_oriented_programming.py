"""
Problem
In past, used procedural or structural programming for stepbystep wise execution
- code duplication
- code maintainance
- data security
- poor code reusability
- no real world representation

"""
warrior_name = "Thor"
warrior_health = 100
warrior_attack = 50

mage_name = "Gandalf"
mage_health = 80
mage_attack = 70

def attack_warrior():
    print('Warrior attacks with power', warrior_attack)

def attack_mage():
    print("Mage attacks with power", mage_attack)

attack_warrior()
attack_mage()

# redundant code, hard to expand, no structure

'''Object oriented programming
- attributes : properties
- behaviour: actions, functions
'''

class Characters:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack_enemy(self):
        print(f'{self.name} attacks with power {self.attack}')
warrior = Characters('Thor', 100, 50)
mage = Characters('Gandalf', 80, 70)
archer = Characters('Archer', 80, 90)

warrior.attack_enemy()
mage.attack_enemy()
archer.attack_enemy()

'''
Classes and Objects
Inheritance
Encapsulattion
Abstraction
Polymorphism
'''
# a class is a blueprint or template for creating objects

# classes and objects
class car():
    def start(self):
        print('Car is starting....')
    def stop(self):
        print('Car is stopping....')

car1 = car()
car2 = car()
car1.start()
car1.stop()
car2.start()
car2.stop()

# adding
class car:
    def set_details(self, brand, color):
        self.brand = brand
        self.color = color

    def show_details(self):
        print(f'This car is a {self.color} {self.brand}')

car1 = car()
car1.set_details('Tesla', 'Red')
car2 = car()
car2.set_details('BMW', 'White')

car1.show_details()
car2.show_details()
