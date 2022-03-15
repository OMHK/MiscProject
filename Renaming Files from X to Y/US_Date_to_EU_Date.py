import shutil as shu
import os
import re
DateUS = re.compile(r"""
^(.*?)
((0|1)?\d)-
((0|1|2|3)?\d)-
((19|20)?\d)
(.*?)$
""", re.VERBOSE)

for filesUS in os.listdir('.'):
    mo = DateUS.search(filesUS)
    if mo is None:
        continue

    partA = mo.group(1)
    partB = mo.group(2)
    partC = mo.group(4)
    partD = mo.group(6)
    partE = mo.group(8)

    EU_File_Name = partA + partC + '-' + partB + '-' + partD + partE
    absWorkingDir = os.path.abspath('.')
    filesUS = os.path.join(absWorkingDir, filesUS)
    EU_File_Name = os.path.join(absWorkingDir + EU_File_Name)
    print('Renaming "%s" to "%s"...' % (filesUS , EU_File_Name ))
    #shutil.move(amerFilename, euroFilename)
