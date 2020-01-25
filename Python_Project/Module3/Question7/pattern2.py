a=int(input("Enter Number of rows -: "))
'''for i in range(a-1):
    print()
    for j in range(a-i):
        print('* ',end='')
for i in range(a+1):
    for j in range(i):
        print('* ',end='')
    print()'''
x=a-1
i=0
while(i<2*a):
    j=0
    while j<x:
        print('* ',end='')
        j=j+1
    print()
    i=i+1
    x=x-1
'''
for i in range(a):
    if i==a//2:
        for k in range(a):
            print(" *",end='')
    else:
        for j in range(a*2):
            if j==a:
                print("* ",end='')
            else:
                print(" ",end='')
    print()
for i in range(a):
    
    for k in range((a-i)):
        print(" ",end='')
    for j in range(i+1):
        print(' *',end='')
    print()

for i in range(a-1):
    print(" ",end='')
    for k in range(i+1):
        print(" ",end='')
    for j in range(a-i-1):
        print(' *',end='')
    print()

print()
for i in range(a-1):
    for k in range((a-i)):
        print(" ",end='')
    for j in range((i*2)+1):
        if j==i*2-1 or j==0:
            print(' *',end='')
        else:
            print(" ",end='')
    print()
    if i==a-2:
        print(" ",end='')
        for k in range(a):
            print(" *",end='')
    
 
'''
