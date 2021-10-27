from tkinter import *
import tkinter
win = tkinter.Tk()
win.geometry('720x300')
win.title('Simple Calculator by Raunak')
win.configure(bg='blue')
win.iconbitmap('Brand-Logo-Icon.ico')
def proces():
    number1=Entry.get(fnE)
    number2=Entry.get(snE)
    operator=Entry.get(oE)
    number1=int(number1)
    number2=int(number2)
    if operator =="+":
        answer=number1+number2
    if operator =="-":
        answer=number1-number2
    if operator=="*":
        answer=number1*number2
    if operator=="/":
        answer=number1/number2
    aL.config(text=answer)
appname = Label(win,text='My Calculator',font=("arial",20,"bold"),bg='blue',fg='red')
appname.grid(row=0,columnspan=40)
fn = Label(win,text='First Number:',font=("arial",15,"bold"),bg='blue',fg='red')
fn.grid(row=1,column=0)
fnE= Entry(win,bd=5)
fnE.grid(row=1,column=1)
sn = Label(win,text='Scond Number:',font=("arial",15,"bold"),bg='blue',fg='red')
sn.grid(row=2,column=0)
snE= Entry(win,bd=5)
snE.grid(row=2,column=1)
o = Label(win,text='Operator',font=("arial",15,"bold"),bg='blue',fg='red')
o.grid(row=3,column=0)
oE= Entry(win,bd=5)
oE.grid(row=3,column=1)
a = Label(win,text='Answer:',font=("arial",15,"bold"),bg='blue',fg='red')
a.grid(row=4,column=0)
aL= Label(win,text="")
aL.grid(row=4,column=1)
B=Button(win,width=20,height=2, text ="Submit",command = proces,bg='yellow').grid(row=5,column=1,)
l = Label(win,text="Operators: Use '+' for addition, '-' for subtraction, '*' for multiplication, '/' for division.",font=("arial",13,"bold"),bg='blue',fg='black')
l.grid(row=6,column=0,columnspan=40)
l.config(anchor=CENTER)
win.mainloop()
