from tkinter import *
import os
os.system('cls')
#***********************
win=Tk()
win.geometry('500x500+700+150')
win.title('phone book')
#******************************************
def mom():
    lb.config(text='sorry mom kheyli dost darm bebakhshid❤😢',font='tahoma')
    

images=PhotoImage(file='add.png')
bu1=Button(image=images,bg='red',command=mom)
bu1.place(x=40,y=20,width=100,height=100)
lb=Label(bg='red',text='..')
lb.place(x=40,y=150,width=400,height=100)









































mainloop()




































