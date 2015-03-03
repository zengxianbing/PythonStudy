__author__ = 'xianbing'

def sayHello():
    print('Hello World!')

sayHello()

def printMax(a,b):
    if a>b:
        print(a,'is maximum')
    else:
        print(b,'is maximum')

printMax(3,4)

def func(x):
    print('x is',x)
    x=2
    print('Changed local x to',x)
x=50
func(x)
print('x is still',x)

def func():
    global  x
    print('x is',x)
    x=2
    print('Changed local x to',x)
x=50
func()
print('Value of x is',x)


def say(message,times=1):
    print(message*times)

say('Hello')
say('World',5)


def func(a,b=5,c=10):
    print('a is',a,'and b is','and c is',c)
func(3,7)
func(25,c=24)
func(c=50,a=100)

def maximum(x,y):
    if x>y:
        return x
    else:
        return  y

print(maximum(2,3))


def printMax(x,y):
    '''Prints the maximum of two numbers

    The two values must be integers.
    '''
    x=int(x)
    y=int(y)
    if x>y:
        print(x,'is maximum')
    else:
        print(y,'is maximum')
printMax(3,5)
print(printMax.__doc__)











