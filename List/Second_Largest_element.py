# Second largest element in List

def secondLargest(l):
    # checking if element in list is less than 2
    if len(l) < 2:
        return "List having less than 2 elements"
    
    # main logic
    larget = 0
    second_larget =0
    for i in l:
        if larget < i:
            second_larget = larget
            larget = i
        elif second_larget < i and larget != i:
            second_larget = i

    return second_larget

l1 = [2,3,6,1,3,5,7,4,8]
print(secondLargest(l1))