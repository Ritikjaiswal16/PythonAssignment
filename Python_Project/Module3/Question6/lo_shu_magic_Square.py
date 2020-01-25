import sys
ls=[]
ls.append(list(map(int,input("Enter the first three -: ").strip().split())))
ls.append(list(map(int,input("Enter the Second three -: ").strip().split())))
ls.append(list(map(int,input("Enter the third three -: ").strip().split())))
sum=ls[0][0]+ls[1][0]+ls[2][0]
if ls[0][0]+ls[0][1]+ls[0][2]!=sum:
    if ls[1][0]+ls[1][1]+ls[1][2]!=sum:
        if ls[0][0]+ls[1][1]+ls[2][2]!=sum:
            print("IT IS NOT")
            sys.exit()
print("YES IT IS")
