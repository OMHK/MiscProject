import re
import pyperclip as pyc


PhoneNumberRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? 
(\s|-|\.)? 
(\d{3}) 
(\s|-|\.) 
(\d{4}) 
(\s*(ext|x|ext.)\s*(\d{2,5}))?
)''', re.VERBOSE)
EmailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[A-Za-z0-9-]+
(\.[a-zA-Z]{2,4})
)''',re.VERBOSE)
text = str(pyc.paste())
listN = []
listE = []
E = 0
for groups in PhoneNumberRegex.findall(text):
    phonenums = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phonenums += ' x' + groups[8]
    listN.append(phonenums)
for groups in EmailRegex.findall(text):
    mails = ''.join(groups[0])
    listE.append(mails)
if len(listN) > 0:
    pyc.copy('\n'.join(listN))
print('List of Numbers has been copied to your clipboard.')
print('input 1 to continue')
E = input()
pyc.copy(E)
if E == True:
    star = True
if len(listE) > 0:
    N = ' \n '.join(listE)
    pyc.copy(N)
print('List of Emails has been copied to your clipboard.')
print('Thank you for using this code :)')
## print(listE)
## print(N)

