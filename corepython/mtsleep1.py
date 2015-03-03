__author__ = 'xianbing'
import thread
from time import sleep,ctime

def loop0():
    print ctime()
    sleep(4)
    print ctime()

def loop1():
    print ctime()
    sleep(2)
    print ctime()
def main():
    print ctime()
    thread.start_new_thread(loop0,())
    thread.start_new_thread(loop1,())
    sleep(6)
    print ctime()

if __name__ == '__main__':
    main()






