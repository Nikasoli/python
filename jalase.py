import termcolor2
txt=input('type your txt ')
x=input('what do you want? ')
if txt.count(x)==0:
    color ='red'
    print(termcolor2.colored('not found!please try again', color))
elif txt.count==1:
    print(txt.index(x)+1)
else:
    print(txt.count(x))
    y=int(input('What do you want?'))
    new_txt=txt.replace(x , '#' , y-1)
    print(new_txt.index(x)+1)

