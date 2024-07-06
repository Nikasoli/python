
import os
import termcolor2
os.system('cls')


lst=[]
def clear():
    input()
    os.system('cls')
    


#*******************************************
while True:
    print('='*30)
    print('welcome to your phone number')
    print('='*30)
    print('1- add number\n2- search number\n3- delete number\n4- show all number\n0- exit')
    color='red'
    x=input(termcolor2.colored(f'what do you want? 0-4 ',color))
    if x=='1':
        color='green'
        name=input(termcolor2.colored(f'type her/his name: ',color))
        num=input(termcolor2.colored(f'type her/his number: ',color))
        full=(f'{name}:{num}')
        lst.append(full)
        clear()
    elif x=='2':
        color='green'
        sname=input(termcolor2.colored(f'type her/his name: ',color))
        for i in lst:
            if sname==i.split(':')[0] or sname==i.split(':')[1]:
                print(i)
                clear()
                break
        else:
                print('not found!!')
    elif x=='3':
        color='green'
        dname=input(termcolor2.colored(f'what do you want to delete?  ',color))
        for i in lst:
            if dname==i.split(':')[0]:
                lst.remove(i)
                print(lst)
                clear()
    elif x=='4':
        for i in lst:
            print(i)
        clear()
            
    elif x=='0':
        color='blue'
        print(termcolor2.colored(f'Are you sure? ',color))
        print('yes:exit\nno:continue')
        yn=input('yes or no? ')
        if yn=='yes':
            print('good bye👋')
            break
        else:
            clear()
    else:
        print('some thing was wrong')
        clear()
            


        

        













