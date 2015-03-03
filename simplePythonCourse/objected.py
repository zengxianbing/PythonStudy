__author__ = 'xianbing'

class Person:
    pass
p=Person()
print(p)

class Person:
    def sayHi(self):
        print('Hello,how are you？')

p=Person()
p.sayHi()

class Person:
    def __init__(self,name):
        self.name=name
    def sayHi(self):
        print('Hello,my name is',self.name)

p=Person('Swaroop')
p.sayHi()


class Person:
    '''Represents a person.'''
    population=0

    def __init__(self,name):
        '''Initializes the person 's data,'''
        self.name=name
        print('(Initializing)%s'%self.name)
        Person.population+=1

    def __del__(self):
        '''I am dying'''
        print('%s says bye.'%self.name)

        Person.population-=1

        if Person.population==0:
            print('I am the last one.')
        else:
            print('There are still %d people left.'%Person.population)


    def sayHi(self):
        '''Greeting by the person.'''

        print('Hi,my name is %s.'%self.name)

    def howMany(self):
        '''Prints the current population.'''
        if Person.population==1:
            print('I am the only person here.')
        else:
            print('We have %d persons here:'%Person.population)


swaroop=Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()

kalam=Person('Abdul Kalam')
kalam.sayHi()
kalam.howMany()

class SchoolMember:
    '''Represents any school member.'''
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('Initialized SchoolMember:%s'%self.name)

    def tell(self):
        '''Tell my details.'''
        print('Name:"%s" Age:"%s"'%(self.name,self.age))


class Teacher(SchoolMember):
    '''Represents a teacher'''
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary=salary
        print('Initialized Teacher:%s'%self.name)

    def tell(self):
        SchoolMember.tell(self)
        print('Salary:"%d"'%self.salary)

class Student(SchoolMember):
    '''Represents a student'''
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks=marks
        print('Initialized Student:%s'%self.name)
    def tell(self):
        SchoolMember.tell(self)
        print('Marks:"%d"'%self.marks)
t=Teacher('Mrs.Shrividya',40,3000)
s=Student('Swaroop',22,75);

members=[t,s]
for member in members:
    member.tell()


























