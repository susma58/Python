'''
Python Dictionary
1- Definition & characteristics
key-value pairs
unordered (before python 3.7)
Mutable

2- Creation
Using {} braces
Using dict() constructor

3- Operations
Adding items
Updating items
Deleting items

4- Dictionary Methods
get(), keys(), values(), items()
pop(), popitem(), clear()

5- Comprehension
Dictionary comprehension

6- Nested Dictionaries

7- Common use cases

'''

my_dict = {
    "Name": "Susma", "Age": 100, "Marks":250, "list": [2,3,4]

}
print(my_dict)
my_dict['Price'] = 1000
print(my_dict)

# updating elements
my_dict["Price"] = 499
print(my_dict)

# if key_name is same then only value will get updated 
# but if key_name is different, then key pair will get added

# deleting the key pairs
del my_dict["Age"]
print(my_dict)

# Methods of dictionary
# get method
profile = {
    'name': 'raju', 'age': 100, 'salary':25000
}
age = profile.get('age', 'Not found')
print(age)

# keys method
keys = profile.keys()
print(list(keys))
print(list(profile.values()))
print(list(profile.items()))




for i in profile:
    print(i)

popped = profile.pop('name')

print(popped)
print(profile)
popped_i = profile.popitem()
print(popped_i)
print(profile)

# clear method
profile = {
    'name': 'raju', 'age': 100, 'salary':25000
}
cleared = profile.clear()
print(profile)

# dictionary comprehension
squares = {x: x*x for x in range(1,20)}

print(squares)

# Nested dictionary
programming_language = {
    "python": {"name": "python", "use_case":['ai, ml, webdev, ds']}
    ,"java": {"name": "java", "use_case": ['app_dev']}
}
print(programming_language)

# loops in dictionary
profile = {
    'name': 'raju', 'age': 100, 'salary':25000
}
for k in profile:
    print(k)

for i in profile.values():
    print(i)