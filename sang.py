from tkinter import*
from random import*
from tkinter import messagebox
import os
#****************************************************************
c_scour=0
u_scour=0
lst=['sang','kaghaz','gheychi']
c=choice(lst)
#*****************************************************************
def sang():
    global c_scour
    global u_scour
    if c=='sang':
        lbl2.config(text='equal')
    elif c=='kaghaz':
        c_scour+=1
        lbl2.config(text=f'computer:{c_scour} user:{u_scour}  computer win')
    elif c=='gheychi':
        u_scour+=1
        lbl2.config(text=f'computer:{c_scour} user:{u_scour}    You win')
def kaghaz():
    global c_scour
    global u_scour
    if c=='sang':
         u_scour+=1
         lbl2.config(text=f'computer:{c_scour} user:{u_scour}  You win')
    elif c=='kaghaze':
        lbl2.config(text='equal')
    elif c=='gheychi':
        c_scour+=1
        lbl2.config(text=f'computer:{c_scour} user:{u_scour}  computer win')
def gheychi():
    global c_scour
    global u_scour
    if c=='sang':
         c_scour+=1
         lbl2.config(text=f'computer:{c_scour} user:{u_scour}  computer win')
    elif c=='kaghaz':
        u_scour+=1
        lbl2.config(text=f'computer:{c_scour} user:{u_scour}  You win')
    elif c=='gheychi':
        lbl2.config(text='equal')
def winner():
    global u_scour
    global c_scour
    if u_scour>c_scour:
        lbl2.config(text='user win')
    elif u_scour<c_scour:
        lbl2.config(text='computer')
    elif u_scour==c_scour:
        lbl2.config(text='equal')
def reset():
    global u_scour
    global c_scour
    mes=messagebox.askokcancel('WARRING!','Are you sure')
    if mes==True:
        u_scour=0
        c_scour=0
#*********************************W********************************
win=Tk()
win.geometry('490x450+400+100')
win.title('game of iran')
win.config(bg='purple')
win.iconbitmap('icon.ico')
#**********************************L*********************************
lbl1=Label(text='wlecome to game',font='tahoma',bg='pink')
lbl2=Label(text='...',font='tahoma')
lbl1.place(x=0,y=0,width=500,height=100)
lbl2.place(x=0,y=300,width=500,height=100)
#***********************************B*******************************
imagb=PhotoImage(file='rock.png')
b1=Button(image=imagb,command=sang)
imagb2=PhotoImage(file='paper.png')
b2=Button(image=imagb2,command=kaghaz)
imagb3=PhotoImage(file='scissor.png')
b3=Button(image=imagb3,command=gheychi)
b1.place(x=20,y=150,width=125,height=125)
b2.place(x=180,y=150,width=125,height=125)
b3.place(x=350,y=150,width=125,height=125)
b4=Button(text='winner',font='tahoma',bg='red',command=winner)
b4.place(x=10,y=0,width=95,height=95)
b5=Button(text='reset',bg='red',font='tahoma',command=reset)
b5.place(x=380,y=0,width=95,height=95)


















































win.mainloop()
