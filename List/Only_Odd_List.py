def findOdd(l):
    for i in range(len(l)):
        c = l.count(l[i])
        if(c%2!=0):
            res = l[i]
            break
    return res

lis = [10,20,10,30,30]
res = findOdd(lis)
print(res) 