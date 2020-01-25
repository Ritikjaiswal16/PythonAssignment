def getItem(room,item):
    ls=datastore['office']['medical']
    for i in ls:
        if i['room-number']==room:
            return i[item]
    return 'empty'

def setItem(room,item,value):
    ls=datastore['office']['medical']
    for i in ls:
        if i['room-number']==room:
            i[item]=value
            return 'done'
    return 'empty'

def options():
    print()
    print("Choose One Option index -: ")
    print("1.Set an Item value")
    print("2.Get an Item value")
    print("3.Room Details")
    return int(input())

def Items():
    print()
    print("Select Item ")
    print("1.room-number")
    print("2.Use")
    print("3.sq-ft")
    print("4.price")
    x=int(input())
    if x==1:
        return 'room-number'
    elif x==2:
        return 'use'
    elif x==3:
        return 'sq-ft'
    elif x==4:
        return 'price'
    else:
        return 'X'

def mode():
    print()
    print("Select Mode -: ")
    print("1.User")
    print("2.Admin")
    return int(input())

def lists():
    for i in datastore.keys():
        print(i)
        for j in datastore[i].keys():
            print("   ",j)
            for k in datastore[i][j]:
                print("      ",k)

def userMenu():
    a=options()
    if a<=0 or a>=4:
        print("Invalid")
    elif(a==1):
        item=Items()
        if item=='X':
            print("Invalid")
            pass
        r=int(input("Enter Room Number -: "))
        val=input("Enter the Value")
        print(setItem(r,item,val))
    elif a==2:
        item=Items()
        r=int(input("Enter Room Number -: "))
        print(getItem(r,item))
    elif a==3:
        r=int(input("Enter Room Number -: "))
        detail(r)

def detail(room):
    c=True
    ls=datastore['office']['medical']
    for i in ls:
        if i['room-number']==room:
            c=False
            print("Room Number     = ",i['room-number'])
            print("Use             = ",i['use'])
            print("Size (in sq-ft) = ",i['sq-ft'])
            print("Price           = ",i['price'])
    if c:
            print("Room Not Found")   
def add_Room():
    number=int(input("Room Number -: "))
    use=input("Room Use -: ")
    size=input("Room Size in sq-ft -: ")
    price=input("Price of the Room -: ")
    datastore['office']['medical'].append({"room-number":number,'use':use,'sq-ft':float(size),'price':float(price)})
    return True
def delete_Room(room):
    ls=datastore['office']['medical']
    for i in range(len(ls)):
        if ls[i]['room-number']==room:
            del ls[i]
            print("DELETED")
 
    
def adminMenu():
    if add_Room():
        print("Added")
    lists()

datastore={'office':{"medical":[{"room-number":100,'use':"reception",'sq-ft':50,'price':75},
                                {"room-number":101,'use':"waiting",'sq-ft':250,'price':75},
                                {"room-number":102,'use':"examination",'sq-ft':125,'price':150},
                                {"room-number":103,'use':"examination",'sq-ft':125,'price':150},
                                {"room-number":104,'use':"ofiice",'sq-ft':150,'price':100}],
                     'parking':{'location':'premium','style':'covered','price':750}}}
m=mode()
if m==1:
    ch=1
    while(ch==1):
        userMenu()
        ch=int(input("Press 1 to go to main menu"))
    
else:
    adminMenu()
    
