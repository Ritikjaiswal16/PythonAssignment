from tkinter import *
from tkinter import messagebox
def get_value():
    label=Label(window,text="Welcome").grid(row=5,column=1)
    response2=messagebox.askquestion("Tricky Question","Do You Want To Save Your Password")
    response1=messagebox.showinfo("Alert Message","Your Response Is Recorded")


window=Tk()
window.title("Form")
a="C:\\Users\\Ritik\\Downloads\\1.png"
icon=PhotoImage(file=a)
label0=Label(window,text="Welcome User",image=icon).grid(row=0,column=3)
label1=Label(window,text="Username").grid(row=1,column=0)
username=Entry(window).grid(row=1,column=1)
label2=Label(window,text="Password").grid(row=2,column=0)
password=Entry(window).grid(row=2,column=1)
checkvalue=IntVar()
check=Checkbutton(window,text="I Agree",variable=checkvalue,onvalue=1,offvalue=0).grid(row=3,column=0)
button=Button(window,text="Login",command=get_value).grid(row=4,column=0)
window.mainloop()
