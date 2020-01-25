from itertools import combinations
def countPairs(ls,sum):
    pair=list(combinations(ls,2))
    check=[]
    for i in pair:
        if int(i[0])+int(i[1])==sum:
            check.append(i)
    return check

ls1=[2,4,5,3,1,6,7]
ls2=[1,2,3,2,4,3]
sum=5
print(list(countPairs(ls1,sum)))
print(list(countPairs(ls2,sum)))
