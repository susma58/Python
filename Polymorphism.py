'''
One name, many forms

Run
person can run fast
car runs on petrol
computer program run smoothly

1 word = run
'''

print(len('Python'))
print(len((1,2,3)))
print(len({'a':1, 'b':2, 'c':3}))

# polymorphism with classes
class bird():
    def sound(self):
        print('Birds make sounds.')

class crow(bird):
    def sound(self):
        print('Crows say "Caw caw"')

class parrot(bird):
    def sound(self):
        print('Parrots say "Kaw kaw"')

bird1 = crow()
bird2 = parrot()       

bird1.sound()
bird2.sound()

# operators polymorphism
print(10+5)
print('hello'+'world')
print([1,2]+[3,4])

# Encapsulation: hiding private values
class bankaccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.___balance = balance #private variable

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}.New balance {self.___balance}')


    def get_balance(self):
        return self.___balance #controlled access
    
account = bankaccount('12345', 50000)

account.deposit(2000)
print(account.get_balance())

print(account.___balance)

