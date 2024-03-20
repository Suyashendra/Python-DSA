def largetElement(l1):
    if not l1:
        return None
    x = 0
    for i in range(len(l1)):
        if x < l1[i]:
            x = l1[i]
    return x

l1 = [2,3,6,1,3,5]
# l1 = [] 
print(largetElement(l1))

# Time complexity - O(n)