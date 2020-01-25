l1=[2,3,4,5,7]
l2=[3,5,2,7]
if len(l2)>len(l1):
    ls=l1
    l1=l2
    l2=ls
for x in l1:
    if x not in l2:
        print(x)
