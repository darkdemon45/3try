a=[1,2,3,4,5,6]
b=[6,5,4,3,2,1]
print(list(zip(a,b)))
print(dict(zip(b,a)))

s=[(1,2),(5,9),(5,7),(8,6)]
c,e=list(zip(*s))
print(c)
print(e)