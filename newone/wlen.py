a=int(input("list size")) #smallest
b=[]
d=[]
for i in range(a):
    c=int(input("elements"))
    b.append(c)
print(b)
for r in (b):
    if (r>b[1]):
        print("hello")
        d=b[1]
        b[1]=b[2]
        b[2]=d