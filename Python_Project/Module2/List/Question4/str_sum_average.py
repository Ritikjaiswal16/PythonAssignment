s=input("Enter-: ").split('=')
sum=u=0
for i in s:
    k=i.split(' ')
    for x in k:
        if x.isnumeric():
            u=u+1
            sum=sum+int(x)
print("sum = ",sum," percentage = ",sum/u)
