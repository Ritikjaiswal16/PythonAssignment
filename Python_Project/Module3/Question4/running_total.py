n,m=map(int,input().split())
ls=list(map(int,input().strip().split()))
max=0
for i in range(n):
    sum=0
    k=i
    for j in range(m):
        if k==n:
            k=0
        sum=sum+ls[k]
        k=k+1
    if sum>max:
        max=sum
print(max)
            
    
    
