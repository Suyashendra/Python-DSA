def reverseArray(l):
    start = 0
    end = len(l)-1
    while start < end:
        l[start], l[end] = l[end], l[start]
        start += 1
        end -= 1
    return l

lis = [1,2,3,4,5,6]
res = reverseArray(lis)
print(res)


# Time Complexity: O(n) -> Linear because loop running through half way.
# Space Complexity: O(1) -> In-place reversal, meaning it doesn’t use additional space.
