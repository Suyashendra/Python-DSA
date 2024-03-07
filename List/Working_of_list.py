# Internal working of List

# List mainly uses Array Data Strucuture as underlying Data Strucuture.

# Array store elements as contiguous memory location

# In Python List can have any type of data in same list.
# Eg: l1 = ['a', 1, 5, 4.2, "Hello"]
# So, List is a Array of reference in Python.
# References are present in contigues memory locations but elements in list are not at 
# contigues memory location.

# List container is a dynamic sized array.

# List Advantages
# 1. List have random access using indexes. So in List we can get element in constant time.
# Set and Dictionary containers don't have random access.

# 2. Cache friendly 

# 3. append() and pop() functions in list takes constant time.
# append() - appends or adds the element in the end to list.
# pop()- pops or removes the element from the end or last element.
# That's why both takes constant time in worst case, O(1).

# List Disadvantages
# 1. Insertion and deletion is slow.
# Insertion and deletion takes linear time O(n). 
# for eg: l = [1,2,3] if we insert 0 at the starting of list than we have to move all elements
# by one position, l = [0,1,2,3]. similarly we have to move elements if we delete any element.

# 2. Search is also slow for unsorted list
# If list is sorted it can use binary search.

# Set is faster than List in Insert, Delete and Search operation.
# Set is unordered.






