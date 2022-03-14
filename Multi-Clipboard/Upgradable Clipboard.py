import shelve as sh
import pyperclip as pyp
import sys
mcshelve = sh.open('mcb')
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcshelve[sys.argv[2]] = pyp.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyp.copy(str(list(mcshelve.keys())))
    elif sys.argv[1] in mcshelve:
        pyp.copy((mcshelve[sys.argv[1]]))

mcshelve.close()
