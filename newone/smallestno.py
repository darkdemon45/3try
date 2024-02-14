a=int(input("list size="))
d=[]
for i in range(a):
    b=int(input("list elements="))
    d.append(b)
for r in range(0,len(d)):
    for j in range(r+1,len(d)):
        if(d[r]>d[j]):
            c=[]
            c=d[r]
            d[r]=d[j]
            d[j]=c
print(d[0])
print(d[1])