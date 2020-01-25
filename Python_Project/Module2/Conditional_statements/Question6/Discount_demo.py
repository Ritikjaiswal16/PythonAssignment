i=int(input("Enter the Number of Package Purchased -: "))
cost=i*99
if(i>=10 and i<=19):
    discount=cost/10
    cost=cost-discount
    print("Discount = ",discount)
elif(i>=20 and i<=49):
    discount=cost/20
    cost=cost-discount
    print("Discount = ",discount)
elif(i>=50 and i<=99):
    discount=cost/30
    cost=cost-discount
    print("Discount = ",discount)
elif(i>=100):
    discount=cost/40
    cost=cost-discount
    print("Discount = ",discount)
print("Total Amount = ",cost)
    
    
