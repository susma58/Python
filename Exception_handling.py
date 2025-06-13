"""
What are errors?
- Compile time errors
- Runtime errors
- Logical errors


To handle runtime errors: exceptional handling

Exception -> 
1- Start running
2- warning sign 
3- catch and handle, program crash

exception handling
zerodivision error

try-except block
try - code error
except - 
finally -
to close the file or resources

nested try-except block
"""

try:
    num = int(input('enter a number: '))
    result = 10/num
    print(f'result: {result}')

except ZeroDivisionError:
    print('You cannot divide with 0')

except ValueError:
    print('You cannot divide with string')


# finally block
try:
    file = open('/Users/Susma/Documents/Python/Python_course/tuple.txt', 'r')
    content = file.read()
    print(content)

except FileNotFoundError:

    print('File not found')


finally:
    file.close()
    print('file operation')


# nested-try except block
try:
    num1 = int(input('enter number 1 '))
    num2 = int(input('enter number 2 '))
    try:
        result = num1/num2
        print(f'Result: {result}')
    except ZeroDivisionError:
        print('You cannot divide with zero.')

except ValueError:
    print('You must provide a valid input')


# check password strength project
def check_password(password):
    if len(password) < 8:
        raise Exception("Error: Password must be >= 8 characters")
    print("Password is strong")

try: 
    password = input('Enter a password = ')
    check_password(password)
except Exception as e:
    print(e)
