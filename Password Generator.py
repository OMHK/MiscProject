'''
this code is a programme that creates passwords using lower and capital letters and numbers
you can specify the length of the password
'''

import random as r

poollist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0']
password = ''
value = 0
d = 0
leng = 0
thevers = []
z = True
c = 0
b = 0

def generator(lang):
    global password
    global thevers
    c = 0
    b = 0
    for c in range(lang):
        value = r.randint(0, 61)
        thevers.append(value)
    for b in range(lang):
        password = password + poollist[thevers[b]]


while z:
    print('Please chose a length:')
    leng = input()
    if leng.isdecimal():
        leng = int(leng)
        break
    print('Please enter a number for your length.')
print('Your new password is')
generator(leng)
print(password)
print('please memorise your new password')
print('Thank you for trying this code')
z = False
