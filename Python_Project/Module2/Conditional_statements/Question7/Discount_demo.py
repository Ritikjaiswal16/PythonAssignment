i=int(input("Enter Pocket Number-: "))
if i==0:
    print("Green")
elif((i>=1 and i<=10) or (i>=19 and i<=28)):
    if i%2==0:
        print("The Pocket is black")
    else:
        print("The pocket is red")
elif((i>=11 and i<=18) or (i>=29 and i<=36)):
    if i%2==0:
        print("The pocket is red")
    else:
        print("The Pocket is black")
else:
    print("Invalid Pocket Number")
    
    
