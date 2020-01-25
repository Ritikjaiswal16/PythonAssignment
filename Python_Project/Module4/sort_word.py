i=list(map(str,input().strip().split()))
d=set(i)
d=list(d)
d.sort()
for i in d:
    print(i,end=' ')
