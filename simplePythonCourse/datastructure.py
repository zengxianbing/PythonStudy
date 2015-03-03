__author__ = 'xianbing'
shoplist=['apple','mango','carrot','banana']

print('I have ',len(shoplist),'items to purchase.')

print('These items are:')
for item in shoplist:
    print(item),

shoplist.append('rice')
print('My shopping list is now',shoplist)

shoplist.sort()
print('Sorted shopping list is now',shoplist)

olditem=shoplist[0]
del shoplist[0]
print('I bought the',olditem)
print('My shopping list is now',shoplist)

zoo=('wolf','elephant','penguin')
print('Number of animals in the zoo is',len(zoo))

new_zoo=('monkey','dolphin',zoo)
print('new zoo',len(new_zoo))
print('new zoo are',new_zoo)
print('old zoo',new_zoo[2])
print('Last animal brought form old zoo is',new_zoo[2][2])

age=22
name='Swaroop'
print('%s is %d years old'%(name,age))
print('why is %s playing with that python?'%name)

ab={'Swaroop':'swaroopch@byteofpython.info',
     'Larry':'larry@wall.org',
     'Matsumoto':'matz@ruby-lang.org',
     'Spammer':'spammer@hotmail.com'
    }
print("Swaroop's address is %s"%ab['Swaroop'])
ab['Guido']='guido@python.org'
del ab['Spammer']

for name,address in ab.items():
    print('Contact %s at %s '%(name,address))

if 'Guido' in ab:
    print("\nGuido's address is %s"%ab['Guido'])

shoplist=['apple','mango','carrot','banana']

print('Item 0 is',shoplist[0])
print('Item 1 is',shoplist[1])
print('Item 2 is',shoplist[2])
print('Item -1 is',shoplist[-1])

name='Swaroop'

if name.startswith("Swa"):
    print("Yes,the string starts with Swa");
if 'a' in name:
    print('Yes,it contains the string "a"')

if name.find('war')!=-1:
    print('Yes,it contains the string "war"')

delimiter="_*_"
mylist=['Brazil','Russia',"India","China"]
print(delimiter.join(mylist))











