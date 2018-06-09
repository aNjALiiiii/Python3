#Ques1 Create a class Animal as a base class and define method animal_attribute.
#  Create another class Tiger which is inheriting Animal and access the base class method.
class Animal():
    def animal_attribute(self):
        print('walk')
        print('eat')
        print('sleep')
class Tiger(Animal):
    def property(self):
        print('attack')
obj = Tiger()
obj.animal_attribute()
obj.property()

#Ques2 What will be the output of following code.
'''class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print(a.f(), b.f())
print(a.g(), b.g())'''
print('Output will be: \nA B\nA B')

#Ques3 Create a class Cop. Initialize its name, age , work experience and designation.
#  Define methods to add, display and update the following details.
# Create another class Mission which extends the class Cop. Define method add_mission _details.
# Select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission.

class Cop():
    def __init__(self,name,age,experience,designation):
        self.name = name
        self.age = age
        self.experience = experience
        self.designation = designation
        self.a=0
    def display(self):
        print('name: %s\nage: %s\nwork experience: %s\ndesignation: %s'%(self.name,self.age,self.experience,self.designation))
        if(self.a==1):
            print('new data: %s'%(self.add1))
    def add(self):
        print('what you want to add')
        self.add1 = input()
        self.a=1
    def update(self):
        print('UPDATE \n1.name\n2.age\n3.work experience\n4.designation\nENTER YOUR CHOICE')
        b = 1
        while (b == 1):
            ch = int(input())
            if (ch == 1):
                print('Enter  name')
                self.name = input()
            elif (ch == 2):
                print('Enter age')
                self.age = input()
            elif (ch == 3):
                print('Enter work experience')
                self.experience = input()
            elif (ch == 4):
                print('Enter designation')
                self.designation = input()
            else:
                print('Enter valid choice')
            print('Again wanna update? if yes press 1 else 2')
            b = int(input())

class Mission(Cop):
    def __init(self):
        super(Mission,self).__init()
    def mission_detail(self):
        self.detail = input()
    def display_mission(self):
        print('mission detail: %s'%(self.detail))
mission = Mission('abc',27,'4 years','xyz')
mission.add()
mission.mission_detail()
mission.display_mission()
mission.display()


#Ques 4  Create a class Shape.Initialize it with length and breadth Create the method Area.
        # Create class rectangle and square which inherits shape and access the method Area.
class Shape():
    def __init__(self):
        self.length = 4
        self.breadth = 3
    def Area(self):
        self.area1 = self.length*self.breadth
        print('area is: %d'%(self.area1))
class rectangle(Shape):
    def detail(self):
        print('for rectangle:')
        self.length = int(input('Enter length'))
        self.breadth = int(input('Enter breadth'))
class square(Shape):
    def detail(self):
        print('for square')
        self.length = int(input('Enter length'))
        self.breadth = int(input('Enter breadth'))
r = rectangle()
s = square()
r.detail()
r.Area()
s.detail()
s.Area()



