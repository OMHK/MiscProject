import shutil as shu
import os
import pathlib as p
import send2trash as s2t
import zipfile as z
## shu.copy(r'C:\Users\omhk9\Desktop\New folder\Python lib installer.txt',r'C:\Users\omhk9\Desktop') ## copying a file
## shu.move(r'C:\Users\omhk9\Desktop\New folder\New Text Document88.txt',r'C:\Users\omhk9\Desktop')  ## moving a file
## shu.move(r'C:\Users\omhk9\Desktop\New folder\New Text Document88.txt',r'C:\Users\omhk9\Desktop\New Text Documentnew.txt')  ## moving a file with a specific name and can also be used to rename a file
## os.unlink(r'C:\Users\omhk9\Desktop\New folder\New Text Document88.txt') ## used to delete a file
## os.rmdir(r'C:\Users\omhk9\Desktop\New folder') ## used to delete an empty folder
## shu.rmtree(r'C:\Users\omhk9\Desktop\New folder') ## used to delete a folder and its contents
##"""for filename in p.Path.home().glob('*.txt'):
  ##  os.unlink(filename) """ ## used to delete all files with the extension .txt
## s2t.send2trash(r'C:\Users\omhk9\Desktop\New folder\New Text Document88.txt') ## Send a file or folder to trash

##for folderName, subfolders, filenames in os.walk(r'C:\Users\omhk9\Desktop\New folder'): ##This command is used to list the contents of a folder
##    print('The current folder is ' + folderName)
##    for subfolder in subfolders:
##        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
##    for filename in filenames:
##        print('FILE INSIDE ' + folderName + ': '+ filename)
##    print('')

## pathy = r'C:\Users\omhk9\Desktop\NewDirFolder'
## examplezip = z.ZipFile( pathy / 'omhk.zip')
## print(examplezip.namelist())
## x = examplezip.getinfo()
## print(x)
## print(x.file_size)
## print(x.compress_size)
## examplezip.close()

## examplezip.extract() ## used to extract zipfiles

## newZip = z.ZipFile('new.zip', 'w')
## newZip.write('filesname',compress_type = z.ZIP_DEFLATED)
## newZip.close()

## page(282)