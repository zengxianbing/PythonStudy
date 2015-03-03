__author__ = 'xianbing'
# -*- coding: utf-8 -*-
import sys
import os
import shutil
dir="c:"
class Packages:
    def __init__(self,srcdir,desdir):
        self.sdir=srcdir
        self.ddir=desdir
    def check(self):
        print('program start....')
        for dirpath,dirnames,filenames in os.walk(self.sdir):
            for filename in filenames:
                thefile=os.path.join(dirpath,filenames)
                try:
                    if os.path.splitext(thefile)[1]=='.rpm':
                       if 'inspuer' in os.popen('rpm -qpi'+thefile).read().rstrip():
                           print('Found error package:'+thefile)
                           shutil.copy(thefile,self.ddir)
                           f=open('list.txt','a')
                           f.write(filename,'\n')
                           f.close()
                except IOError,err:
                    print err
                    sys.exit()


if __name__ == '__main__':
    dir=Packages('','')
    dir.check()
