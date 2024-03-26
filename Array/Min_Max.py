# Maximum and Minimum of an Array\

# Approach 

# 1. Sorting

# def min_max(l):
#     #using sort function to sort the list.
#     l.sort()
#     min_val = l[0] # min value will be at index 0
#     max_val = l[-1] # max value will be at index -1 (which is last element)
#     # making an dictionary
#     res = {"min":min_val, "max":max_val}
#     return res


# if __name__ == "__main__":
#     lis = [5,2,3,10,4,1]
#     res = min_max(lis)
#     print("Maximum element in array is: ",res["min"])
#     print("Maximum element in array is: ",res["max"])

# TC: O(n log n), where n is number of elements.
# SC: O(1), as we are not using extra spaces.

# 2. Linear Search

# creating structure to return two values min and max

class pair:
    def __init__(self):
        self.min = 0
        self.max = 0

# main logic function
def getMinMax(arr: list, n: int) -> pair:
    minmax = pair()

    # condition if array has only one element
    if n==1:
        minmax.min = arr[0]
        minmax.max = arr[0]
        return minmax
    
    # if array size is greater than 1 element 
    # initialize min and max
    if arr[0] > arr[1]:
        minmax.min = arr[1]
        minmax.max = arr[0]

    else:
        minmax.min = arr[0]
        minmax.max = arr[1]

    # iterating over array starting from 3rd element (2nd index)
    for i in range(2,n):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]
        
    return minmax

if __name__ == "__main__":
    lis = [5,2,3,10,4,1]
    res = getMinMax(lis,len(lis))
    print("Maximum element in array is: ",res.min)
    print("Maximum element in array is: ",res.max)

# TC: O(n)
# SC: O(1) 