
# Data abstraction
# hiding unneccesary details

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):

        pass #no implementation

class car(Vehicle):
    def start(self):
        print('Car starts with a key.')

class bike(Vehicle):
    def start(self):
        print('Bike starts with a button')

car = car()
bike = bike()

car.start()
bike.start()

