__author__ = 'xianbing'

i=5
print(i)
i=i+1
print(i)
s='''This is a multi-line string.
This is the second line
'''
print(s)

length=5
breadth=2
area=length*breadth
print('Area is',area)
print('Perimeter is ',2*(length+breadth))

number=23
guess=int(input('Enter an integer:'))
if guess==number:
    print("Congratulations,you guessed  it.")
    print("but you do not win any prizes!")
elif guess<number:
    print("No,it is a little higher than that")
else:
    print('No,it is a litte lower than that')

number=23
running=True

while running:
    guess=int(input('Enter an integer:'))

    if guess==number:
        print('Congratulations,you guessed it.')
        running=False
    elif guess<number:
        print('No,it is a little higher than that')
    else:
        print('The while loop is over.')

for i in range(1,5):
    print(i)
else:
    print('The for loop is over')

while True:
    s=input("Enter something:")
    if s=='quit':
        break:
        print('Length of the string is',len(s))
print("Done")

while True:
    s=input('Enter something:')
    if s=='quit':
        break

    if len(s)<3:
        continue
print('Input is of sufficient length')















