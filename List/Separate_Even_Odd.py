def evenOdd(lis):
    even = []
    odd = []
    for i in lis:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)

    return even, odd

l = [10,15,20,25,30,35]
even, odd = evenOdd(l)
print(even)
print(odd)
