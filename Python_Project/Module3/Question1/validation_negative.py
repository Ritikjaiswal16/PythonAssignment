ch='Y'
while ch=='y' or ch=='Y':
    ws=int(input("Enter wholesale price -: "))
    if ws<0:
        print("Invalid price ")
        continue
    print("Retail price = ",ws*0.5)
    ch=input("Press 'y' to calculate more")

    
    
