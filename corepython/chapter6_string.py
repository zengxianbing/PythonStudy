__author__ = 'xianbing'
# -*- coding:utf-8 -*-
import string
from string import Template
names=('aaa','bb','ccc')
print names[1]
s='abcdefg'
print s[::-1]
print s[0:1]
print s[1:]
s=s[1:]+"bbbb"
print s
print names[-100:100]

i=-1
for i in range(-1,-len(s),-1):
    print s[:i]
print
for i in [None] + range(-1,-len(s),-1):
    print s[:i]

print 'bb' in 'bbbbaaaa'

alphas=string.letters+'_'
nums=string.digits
ss='a'
for otherChar in alphas:
    if otherChar not in alphas+nums:
        print 'exits'
        break
else:
    print 'not exist'
s="abcdefg"
length=len(s)
i=0
while i<length:
    print s[i]
    i=i+1
print
for j in range(length):
    print s[j],'(%d)'%j
print
for i,ch in enumerate(s):
    print ch,'(%d)'%i


s=''.join(('aaa','bbb','ccc'))
print s
print u'sdf'
print s*3
print "%+d"%4

s=Template('There are ${howmany} ${lang} Quotation')
print s.substitute(lang='python',howmany=3)
ss='asdfdsf232'
print max(ss)
print min(ss)

for i,t in enumerate(ss):
    print i,t

s,t='foa','obr'
print zip(s,t)

print chr(65)

aList=[123,'abc',4,5,['aaa','bbb'],89]
print aList

print list('foo')
print aList[0]
print aList[0:2]
print aList[2:]
aList[2]='float replacer'
print aList
del aList[1]
print aList
for t in reversed(aList):
    print t
print sorted(aList)

for i,album in enumerate(aList):
    print i,album

fn=['ian','stuart','david']
ln=['barirnson','elliott','paton']
for i,j in zip(fn,ln):
    print ('%s %s'%(i,j)).title()
a=[3,4,5]
print sum(a)
dir(list)
print
print
print

print


aTuple=(123,'abc','33',['inner','tuple'],33)
print aTuple
print aTuple[0:2]
print aTuple[2:]

dict1={}
dict2={'name':'earth','port':80}
print dict1,dict2

fdict=dict((['x',1],['y',2]))
print fdict

ddict={}.fromkeys(('x','y'),-1)
print ddict

edict={}.fromkeys(('foo','bar'))
print edict

dict2={'name':'earth','port':80}
for key in dict2.keys():
    print 'key=%s,value=%s'%(key,dict2[key])
print 'server' in dict2
dict3={}
dict3[1]='abc'
dict3['1']=3.445
dict3[3.2]='xyz'
print dict3
dict3['1']='aaa'
print dict3
del dict2['name']
dict2.clear()
del dict2
#dict2.pop('name')
print dict3.keys()
print dict3.values()
print dict3.items()

for eachKey in sorted(dict3):
    print 'dict3 key',eachKey,'has value',dict3[eachKey]

dict2={'host':'earth','port':80}
dict3={'host':'venus','server':'http'}
dict2.update(dict3)
print dict2

dict4=dict2.copy()
print dict4

s=set('cheeseshop')
print s
t=frozenset('bookshop')
print t
print  type(s)
print  type(t)
s.add('z')
s.update('pypi')
s.remove('z')
s-=set('pypi')
