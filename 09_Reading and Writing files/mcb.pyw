import pyperclip
import shelve
import sys

mcbshelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3:
    if sys.argv[1] == 'save':
        mcbshelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        if sys.argv[2] in mcbshelf:
            del mcbshelf[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbshelf.keys())))
    elif sys.argv[1] in mcbshelf:
        pyperclip.copy(mcbshelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'delete':
        print('Are you sure you want to delete every keyword?')
        if sys.argv[1].lower() == 'yes':
            mcbshelf.clear()
mcbshelf.close()
