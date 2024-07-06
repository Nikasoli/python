import pyfiglet
from price import *
import os
os.system('cls')
while True:
    print(pyfiglet.figlet_format('nika'))
    print('='*20)
    print('welcome')
    print('='*20)
    print('1-apple 🍎')
    print('2-banana 🍌')
    print('3-kiwi 🥝')
    print('4-cherry 🍒')
    print('0-exit 👋')
    num=input('choose one 0 to 4 ')
    if num=='1':
        print('apple:',apple,'$')
        v=int(input('how many? '))
        print('total:', v*apple)
        print('please type end ')
        input()
        os.system('cls')
    if num=='2':
        print('banana:',banana,'$')
        v=int(input('how many? '))
        print('total:', v*banana)
        print('please type end ')
        input()
        os.system('cls')
    if num=='3':
        print('kiwi:',kiwi,'$')
        v=int(input('how many? '))
        print('total:', v*kiwi)
        print('please type end ')
        input()
        os.system('cls')
    if num=='4':
        print('cherry:',cherry,'$')
        v=int(input('how many? '))
        print('total:', v*cherry)
        print('please type end ')
        input()
        os.system('cls')
    if num=='0':
        print('bye bye')
        input()
        break

