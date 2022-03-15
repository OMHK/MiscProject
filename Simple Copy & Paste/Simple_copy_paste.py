#! python3
# Simple_copy_paste.py - A multi-clipboard program.
import pyperclip as pyc
import sys
Dict = {'greeting':'Greetings /n hope that you are doing well',
        'ending':'Excited to hear back from you /n best regards /n Omar H. khasawneh',
        'body':'Yeah I know that'}

if len(sys.argv) < 2:
    print('Usage: python Simple_copy_paste.py [keyphrase] - copy phrase text')

keyphrase = sys.argv[1]

if keyphrase in Dict:
    pyc.copy(Dict[keyphrase])
    print('Text for' + keyphrase + 'copied to clipboard.')
else:
    print('There is no Text for' + keyphrase)