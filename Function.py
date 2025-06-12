'''
Function
reusability
code to perform particular tasks

modularity

scoping

'''
def greet():
    '''displaying a hi message to user'''

    print('Hi')

greet()

# parameters and arguments
# parameters are placeholders for the values
# arguments: values passed
def greet(name): #name=parameter
    print('Hi', name)

greet("susma") #susma=argument
greet("archies")
greet("robot")

'''
Positional arguments
Keyword arguments
Default arguments
'''
# positional arguments
def greet(name, city):
    print(f'Welcome {name} to the {city}')
greet('raju', 'mumbai')

# keyword arguments
def greet(name, city):
    print(f'Welcome {name} to the {city}')
greet(name ='raju',city= 'mumbai')

# default arguments
def greet(name='raju', city='mumbai'):
    print(f'Welcome {name} to the {city}')
greet(name ='shyam',city= 'india')

# Return statement
def get_full_name(first_name, last_name):
    '''return the full name, in a neated format'''
    full_name = f'{first_name} {last_name}'
    print(full_name)

    return full_name


name = get_full_name("gopal", "raju")
print(name)

"""
function naming
length of functions
avoid global variables

"""

# local and global variables
def sum(a,b):
    return a+b

a = 10
b = 20
result = sum(a, b)
print(result)

# global variables are those that are not defined in function
# local variables are accessible only inside the function and built inside the function

def msg():
    # local variable
    choice = "I love coding wise."
    print(choice)

msg()

def msg():
    print("Inside the function", choice)

choice = "I love coding wise." #global variable
msg()

# Decorators
'''
burger = function
extra cheese = extra feature
 
main function : function add
without changing the main function code
'''

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function is called")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()

# Generators
'''
Behave like iterators
use yield keyword
'''
def count_down(num):
    while num>0:
        yield num
        num -= 1

# using the generator
for number in count_down(5):
    print(number)


# lmd function: lambda argument: expression condition
add_tem = lambda x:x+10
print(add_tem(5))
