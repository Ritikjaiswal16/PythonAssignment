import pickle
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
ls=[]
f=open('Contact.txt','wb')
con=Contact()
con.set_name("rtk")
con.set_number('234')
con.set_email('a@123.com')
ls.append(con)
pickle.dump(ls,f)
f.close()
