def average(lis):
    sum = 0
    len = 0
    for x in lis:
        sum = sum + x
        len +=1

    return sum/len

l = [1,2,3,4]
result = average(l)
print(result)

# or 
# def avg(lis):
#     return sum(lis)/len(lis)
# l = [1,2,3,4]
# result = average(l)
# print(result)

