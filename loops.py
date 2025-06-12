"""
repeat multiple times, repititive process
While loop: until and unless condition is True
For loop: only operated according to sequences

"""
i=1
while i<= 5:
    print(i)
    i += 1

a = [1,2,3,4,5]
for i in a:
    print(i)



# range function (start, stop, step)
a = list(range(1,10,1))
print(a)

# Nested loop: work different loops together in one loop
for i in range(1,3):
    for j in range(3,6):
        print(f'{i}, {j}')

# break statement
for num in range(1,10,1):
    if num == 5:
        break

    print(num)



# continue statement
for num in range(1,5):
    if num == 3:
        continue
    print(num)


# pass statement
for num in range(1,10):
    if num == 5: 
        pass
    print(num)



# question 1: extract even numbers from 1-10
for i in range(0,10,2):
    print(i)


for i in range(1,11):
    if i %2 == 0:
        print('even', i)
    else: 
        print('odd', i) 


# another question
i = int(input("Enter the first number: "))
j = int(input("Enter the last number: "))
r = int(input("Enter the range you want: "))
for a in range(i, j, r):
    print(a)


for a in range(i, j):
    if a == r:
        continue
    elif i>j:
        print("Invalid value")
    else:
        print(a)