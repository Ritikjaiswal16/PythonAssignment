from tkinter import *
def clear():
    global expr
    expr=""
    input_text.set("")

def click(item):
    global expr
    expr=expr+str(item)
    input_text.set(expr)

def equal():
    global expr
    result=str(eval(expr))
    inpuy_text.set(expr)

expr=""
window=Tk()
input_text=StringVar()
input_frame=Frame(window,width=)
