import webbrowser
import sys
import pyperclip as pyp
if len(sys.argv) > 1:
    address = ''.join(sys.argv[1:])
else:
    address = pyp.paste()
webbrowser.open('https://www.google.com/maps/place/' + address)
