'''
this code is a programme that creates passwords using lower and capital letters and numbers
you can specify the length of the password
'''

import random as r
import re
import pyperclip as pyc

poollist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0','@','!','#','$','%','^','&','*','(',')','-','=','+','?','<','>']
password = ''
value = 0
d = 0
leng = 0
thevers = []
z = True
your_email = ''
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,3})+')
def generator(lang):
    global password
    global thevers
    c = 0
    b = 0
    for c in range(lang):
        value = r.randint(0, 77)
        thevers.append(value)
    for b in range(lang):
        password = password + poollist[thevers[b]]

def isvalid(email):
    global regex
    global your_email
    while True:
        if re.fullmatch(regex,email):
            print('your email is:')
            print(email)
            break
        print('Invalid Email Please renter')
        email = input()
print('Please enter your email')
your_email = input()
isvalid(your_email)

while z:
    print('Please chose a length: (more than 16 characters is recommended)')
    leng = input()
    if leng.isdecimal():
        leng = int(leng)
        break
    print('Please enter a number for your length.')

print('Your new password is')
generator(leng)
print(password)
pyc.copy(password)
print('please memorise your new password')
print('The password has been copied to your clipboard')
print('Thank you for trying this code')