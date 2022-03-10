import pathlib as pl
import os
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