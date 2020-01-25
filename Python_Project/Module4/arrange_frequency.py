a=list(map(int,input().strip().split()))
b=set(a)
b=list(b)
freq=[]
for i in b:
    freq.append(a.count(i))
del a
c=[]
for i in range(len(b)):
    m=max(freq)
    index=freq.index(m)
    for j in range(m):
        c.append(b[index])
    freq.remove(m)
    del b[index]
print(c)
