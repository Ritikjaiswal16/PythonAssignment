import pickle
import sys
ls=[]
class Contact:
    def __init__(self):
        self.__name=''
        self.__number=''
        self.__email=''
    def set_name(self,name):
        self.__name=name
    def set_number(self,number):
        self.__number=number
    def set_email(self,email):
        self.__email=email
        
    def get_name(self):
        return self.__name
    def get_number(self):
        return self.__number
    def get_email(self):
        return self.__email
    def __str__(self):
        return f'name={self.get_name()} \nphone number={self.get_number()} \nEmail address={self.get_email()} \n'
def search(name):
    f=open('contact.txt','rb')
    try:
        c=list(pickle.load(f))
    except:
        return False
    for j in range(len(c)):
        if c[j].get_name()==name:
            print("\nDATA FOUND")
            f.close()
            print(c[j].__str__())
            return j
    print("\nDATA NOT FOUND")
    return True

def Add():
    ls=read_file()
    ch='y'
    while ch=='y':
        con=Contact()
        con.set_name(input("Name = "))
        con.set_number(input("Contact Number = "))
        con.set_email(input("Your Email"))
        ls.append(con)
        ch=str(input("press y to store more element"))
    update_file(ls)
    print("\nData Inserted Succesfully")


def update(name,att,value):
    ls=read_file()
    a=search(name)
    if a==True:
        return False
    con=Contact()
    con=ls[a]
    if att=='name':
        con.set_name(value)
    elif att=='number':
        con.set_number(value)
    elif att=='email':
        con.set_email(value)
    else:
        return False
    ls[a]=con
    update_file(ls)
    return True
def delete(name):
    ls=read_file()
    a=search(name)
    if a==True:
        return False
    con=Contact()
    del ls[a]
    update_file(ls)
    return True

def read_file():    
    f=open('contact.txt','rb')
    try:
        l=list(pickle.load(f))
    except:
        l=[]
    f.close()
    return l

def update_file(ls):
    f=open('contact.txt','wb')    
    pickle.dump(ls,f)
    f.close()
def print_all():
    ls=read_file()
    f=open('contact.txt','rb')
    c=Contact()
    con=pickle.load(f)
    for j in range(len(con)):
        c=con[j]
        print(c.__str__())
    f.close()




    
while(True):
    print("1.Search for A contact")
    print("2.Add a new contact")
    print("3.update a contact")
    print("4.Delete a contact")
    print("5.Show All Contacts")
    print("6.Quit")
    a=int(input("Choose any option "))
    if a==1:
        i=input("Enter Name to be searched for = ")
        j=search(i)            
    elif a==2:
        Add()
    elif a==3:
        name=input("Enter Name of the contact -: ")
        att=input("Enter ATTRIBUTE TO CHANGE (name/email/number) -: ")
        value=input("Enter new value -: ")
        if update(name,att,value):
            print("\nData Updated Succesfully")
        else:
            print("\nError Occured in Updation")
    
    elif a==4:
        name=input("Enter Name of the contact to be deleted -: ")
        if delete(name):
            print("\nData Deleted Succesfully")
        else:
            print("\nCan't DELETE DATA")
    elif a==5:
        print_all()
    elif a==6:
        print("\nSee You Soon")
        sys.exit()
    else:
        print("\nInvalid Key")
  
