import random
import os
os.system('cls')


frutes=['kiwi','banana','orange','apple','coconat',]
x=(random.choice(frutes))
print(x)
lst=['_']*len(x)
print(lst)
while lst.count('_')>0:
    char=input('type your char ')
    for i in range(len(x)):
        if char==x[i]:
            lst[i]=char
            print(lst)
            
        elif char!=x[i]:
         break
    
else:
        print('very good finishhhh')
        

