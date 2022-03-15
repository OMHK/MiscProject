import pathlib as pl
import os
import shelve as sh
import pprint as pp
myfiles = ['accounts.txt','details.csv','invite.docx']
for filename in myfiles:
    print(pl.Path(r'C:\users\omhk9\Desktop',filename))
print(pl.Path.cwd()) ## finding the current working directory
print(pl.Path.home()) ## finding the home directory of your OS
## os.makedirs('C:\\Users\\omhk9\\Desktop\\NewDirFolder')  ## For creating a new folder
## pl.Path(r'C:\Users\omhk9\Desktop\NewDirFolder').mkdir()
ThePath = pl.Path(r'C:\Users\omhk9\Desktop\spam.txt')
print(ThePath.anchor)
print(ThePath.parent)
print(ThePath.name)
print(ThePath.stem)
print(ThePath.suffix)
print(ThePath.drive)
print(pl.Path.cwd())
print(pl.Path.cwd().parents[0])
print(pl.Path.cwd().parents[1])
print(pl.Path.cwd().parents[2])
print(pl.Path.cwd().parents[3])
print(os.path.getsize(r'F:\Python'))
print(os.listdir(r'F:\\'))
totalsize = 0
for filename in os.listdir('F:\Python'):
    totalsize = totalsize + os.path.getsize(os.path.join('F:\Python',filename))
print(totalsize)
print(totalsize/1024)
p = pl.Path(r'C:\Users\omhk9\Desktop')
pp=pl.Path(r'C:\Users\Public\Desktop\Steam.lnk')
p.glob('*')
print(list(p.glob('*')))
print(p.exists())
print(pp.is_file())
gDrive = pl.Path('G:/')
print(gDrive.exists())
r = pl.Path('spam.txt')
r.write_text('Hello, World')
r.read_text()
helloFile = open(r'C:\Users\omhk9\Desktop\New Text Document (4).txt',)
helloContent = helloFile.read()
print(helloContent)
helloFile.close()
FFile = open(r'C:\Users\omhk9\Desktop\New Text Document (3).txt')
FFContent = FFile.readlines()
print(FFContent)
helloFile = open(r'C:\Users\omhk9\Desktop\New Text Document (4).txt', 'a')
helloFile.write('This world is not for you and I \n')
helloFile.close()
helloFile = open(r'C:\Users\omhk9\Desktop\New Text Document (4).txt')
ConConCon = helloFile.read()
print(ConConCon)
shelfFile = sh.open('mydata')
cats = ['Zophie', 'polka', 'simon']
shelfFile['cats']  = cats
shelfFile.close()
shelfFile = sh.open('mydata')
type(shelfFile)
## shelfFile = shelve.open('mydata)  ''' use these next 3 lines to  open shelve files '''
## type(shelfFile
## shelfFile['cats']
shelfFile.close()
## shelfFile = sh.open('mydata') ''' Use these 3 lines to store files in a list '''
## list(shelfFile.values())
## shelfFile.close()

## dats = [{'nameK' :'zophie', 'desc' : 'chubby'}, {'name':'pooka', 'desc':'fluffy'}]
## pp.pformat(dats)

