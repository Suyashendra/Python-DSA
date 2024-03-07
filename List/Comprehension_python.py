# Comprehension in Python

# List comprehension

# list which contains even numbers (0-10)
even_list = [x for x in range(11) if x%2 == 0]
print(even_list)

# list which contains odd numbers (0-10)
odd_list = [x for x in range(11) if x%2 != 0]
print(odd_list)

# Eg - Create a function for list that contains elements less than x.
def getSmaller(l,x):
    result = [i for i in l if i<x]
    return result

my_list = list(map(int,input("Enter list elements: ").split()))
x = int(input("Enter x value: "))
res = getSmaller(my_list,x)
print(res)

# some more e.g.

s = "HelloWorld"
l1 = [i for i in s if i in "aeiou"]
print(l1)

s1 = ["Hello", "World","New"]
l2 = [i for i in s if i.startswith('W')]
print(l2)

l3 = [i*i for i in range(1,11)]
print(l3)

l4 = ["apple","mango","orange","banana"]
l5 = [i.upper() for i in l4 if i.startswith('a')]
print(l5)

# Set comprehension

l6 = [10,20,3,4,10,20,7,3]
set1 = {i for i in l6 if i%2 ==0}
set2 = {i for i in l6 if i%2 !=0}
print(set1, set2)

# Dictionary Comprehensions

l7 = [1,2,3,4,5]
d1 = {i:i**2 for i in l7}
print(d1)

d2 = {i:f"ID{i}" for i in range(1,6)}
print(d2)

l8 = [101,102,103]
l9 = ['A','B','C']
d3 = {l8[i]:l9[i] for i in range(len(l8))}
print(d3)

# Better approach for above code is
d4 = dict(zip(l8,l9))
print(d4)

# converting key, values of dict into values, keys

d5 = {1:'A',2:'B'}
d6 = { v:k for (k,v) in d5.items()}
print(d6)
