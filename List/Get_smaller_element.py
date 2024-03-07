# Given a list and x element 
# find all element that are less than x.

def getSmaller(lis,x):
    res = []
    for i in lis:
        if(i<x):
            res.append(i)
    return res 

x = 10
l = [8,100,20,40,3,7]
print(getSmaller(l,x))