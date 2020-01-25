from itertools import combinations
ls=[2,3,4,2,5,2,3,1,3,2,4,3,2,3,4]
sum=10
pair=list(combinations(ls,2))
check=True
for i in pair:
    if int(i[0])+int(i[1])==sum:
        print("Yes There Exist Atleast one pair")
        check=False
        break
if check:
    print("NO there exist no  pair ")
    
