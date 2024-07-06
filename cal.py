from tkinter import*
import os
os.system('cls')
#*******************************************
def plus():
    '''جمع دو عدد'''
    num1=int(en.get())
    num2=int(en2.get())
    result=num1+num2
    lbl.config(text=result)
def minus():
    '''تفریق دو عدد'''
    num1=int(en.get())
    num2=int(en2.get())
    result=num1-num2
    lbl.config(text=result)
def multiplied():
    '''ضرب دو عدد'''
    num1=int(en.get())
    num2=int(en2.get())
    result=num1*num2
    lbl.config(text=result)
def divided():
    '''تقسیم دو عدد'''
    num1=int(en.get())
    num2=int(en2.get())
    result=num1/num2
    lbl.config(text=result)
#*******************************************
win=Tk()
win.geometry('500x500')
win.title('calculator')
win.iconbitmap('images/cal.ico')
win.config(bg='purple')
#**************************************
en=Entry(justify='center',font=('tahoma',20))
en2=Entry(justify='center',font=('tahoma',20))
en.place(x=50,y=10,width=400,height=50)
en2.place(x=50,y=65,width=400,height=50)
#******************************************
bt1=Button(text='➕',font=('tahoma',20),command=plus)
bt2=Button(text='➖',font=('tahoma',20),command=minus)
bt3=Button(text='✖',font=('tahoma',20),command=multiplied)
bt4=Button(text='➗',font=('tahoma',20),command=divided)
bt1.place(x=150,y=150,width=100,height=100)
bt2.place(x=260,y=150,width=100,height=100)
bt3.place(x=150,y=270,width=100,height=100)
bt4.place(x=260,y=270,width=100,height=100)
bt1.config(bg='deep pink')
bt2.config(bg='deep pink')
bt3.config(bg='deep pink')
bt4.config(bg='deep pink')
#**********************************************
lbl=Label(justify='center',font=('tahoma',20))
lbl.place(x=150,y=400,width=200,height=50)








win=mainloop()