__author__ = 'xianbing'

import  sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)

if __name__=='__main__':
    print('This program is being run by itself')
else:
    print 'I am being imported from another module'
