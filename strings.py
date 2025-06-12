"""
string and characters
characters: a-z A-Z !@#$
white space

"""

name = 'sagar'
# 3 characteristics
# strings are immutable
# indexed as every elements are indexed
# iterable

a = "python"
print(a[-1])

language = 'python'
for i in language:
    print(i)

# find length of the string (len())
print(len(language))

password = '123#@$python'
if len(password) >= 6:
    print("your password is strong")
else:
    print("Invalid password. Enter again!")


# indexing
text = "Hello. It's me python."
print(text[::-1])

# repeat
number = '10'
hello = 10
print(number * 20) 
print(hello * 20) 

name = ' susma'
last_name = ' regmi'
print('Hi' + name + last_name)

# checking membership
text = 'python is the king.'
# membership operator
print('king' in text)

email = "regmisusma58@gmail.com"
if "@" in email:
    print("Email address is valid.")
else:
    print("Invalid email.")

str = 'THISISPYTHON'
print(str.lower())
# upper case; capitalize
print(str.capitalize())
print(str.title())
print(str.swapcase())

# find method
text = 'python programming'
print(text.find('n'))
# replace method
print(text.replace('python', 'java'))

# splitting method
str = 'a,b,c'
s = str.split(',')
print('after splitting', s)

# joining
result = ', '.join(s)
print(result)

# checking method
"""
start method

"""

str = "python"
print(str.startswith('p'))
print(str.isalpha())
print(str.isalnum())