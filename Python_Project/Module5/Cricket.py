data={}
ch='y'
while(ch=='y'):
   
    typ=input("Enter Type of player -: ")
    name=input("Enter Player name -: ")
    run=int(input("Enter total runs -: "))
    avg=int(input("Enter avg of player -: "))
    high=int(input("Enter highest runs -: "))
    if typ not in data:
        data[typ]={}
    data[typ][name]={'run':run,'avg':avg,'high':high}
    ch=input("want to Enter more players (y) -: ")
    print()
    print()
print(data)
