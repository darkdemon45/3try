def ab(a):
    if(a%2==0):
        return a
a=[1,2,3,5,6,4]
filtered=list(filter(ab,a))
print(filtered)