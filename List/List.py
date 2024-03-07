# List

l1 = [1,2,3,4,5]
print(l1[0])

# List functions
l1.append(6) # add elements at the end of list.
print(l1)

l1.insert(1,1.5) # insert element at a specific index.
print(l1)
print(1.5 in l1) # in operator used to check if a element is present in collection or not. returns Ture or false.

l1.append(5)

c = l1.count(5) # counts element  
print(c)

i = l1.index(5) # return index of first occurence of element in list.
print(i)

i1 = l1.index(2,1,4) # finds 2 from index 1 to 4-1. (element, start-index-inclusive, end-index-exclusive)
print(i1)

l2 = [10,20,30,40,50,60,70,80]

l2.remove(20) # remove given element from list.
print(l2)

print(l2.pop()) # removes and returns last element from the list.

print(l2)

print(l2.pop(1)) # removes and return element based on given index.

print(l2)


# Some general purpose functions of collections.

del l2[1] # del method is general method which can be used on other collection also.
print(l2)

del l2[0:2] # elements can deleted using range of indexes.
print(l2)

l3 = [10,40,20,50] 
print(max(l3)) 
print(min(l3))
print(sum(l3))
print(len(l3))
l3.reverse()
print(l3)
l3.sort() 
print(l3)


