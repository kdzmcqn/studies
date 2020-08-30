'''
f = open('fileName', 'mode', 'buffer')
                     4096, or 8092

'''
f = open('myfile.txt', 'w')
s = input('enter text: ')
f.write(s)
f.close()

# check the file if it exists
import os
import sys

if os.path.isfile('LOL.txt'):
    print('yes')
else:
    print('no')
    sys.exit()
