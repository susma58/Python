# list:: ordered, mutable, dynamic, heterogeneous
# ways of creating list: [], list constructor list(())
# list comprehension and range function

lst = [1,2,3,4,5]
print(lst[0])
lst[0] = 'hello'
print(f'After list {lst}')

lst[0:3] = 10,20,30
print(lst)

# concatenation of list
a = [1,2,3]
b = [4,5,6]
result = a + b
print(result)


lst1 = [1,2,3]
lst2 = lst1.copy()
lst2[0] = 1000
print(lst1, lst2)

# append, extend, insert, pop, count
a = [1,2,3]
a.insert(2, 10)
print(a)

a.remove(3)
print(a)

a.pop(0)
print(a)

a.clear()
print(a)

a = [1,2,3]
index = a.index(2)
print(index)

count = a.count(3)
print(count)

# sorting of elements
a = [5,4,2,6,8,6]
sorted_a = a.sort()
print(a)

# reversing
a.reverse()
print(a)

# copy method
a = [1,2,3]
a_copy = a.copy()
print(a_copy)

# finding max and min values
print(min(a))
print(max(a))

# finding common elements
a = [1,2,3,4]
b = [4,5,6]
s1 = set(a)
s2 = set(b)
s3 = s1.intersection(s2)
print(list(s3))

# nested list
a = [1,2,3]
b = [3,4,5,6, [7,8,8]]
print(b)
