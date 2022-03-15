import pyinputplus as pyip
print('Please input your a string')
string = pyip.inputStr()
x = 1
while x == True:
    try:
        string
    except:
        print('This text won\'t appear')
        continue
    if string is str:
        print('you have entered a string')
        continue
    break
print(f'Your string is {string}')
