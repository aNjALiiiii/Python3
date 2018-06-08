#Ques1 Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.
import math
class circle():
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return math.pi * (self.radius ** 2)

    def getCircumference(self):
        return 2 * math.pi * self.radius


r = int(input("Enter radius of circle: "))
obj = circle(r)
print("Area of circle:", round(obj.getArea(), 2))
print("circumference of circle:", round(obj.getCircumference(), 2))

#Ques2 Create a Student class and initialize it with name and roll number. Make methods to :
#1. Display - It should display all informations of the student.
class Student():
    def __init__(self,name,rolln):
        self.name = name
        self.rolln = rolln
    def display(self):
        print('student name:')
        print('name: %s'%(self.name))
        print('roll no: %s '%(self.rolln))
name = input('enter the name of student ')
rolln = input('enter roll no of student ')
obj1 = Student(name,rolln)
obj1.display()

#Ques3 Create a Temprature class. Make two methods :
#1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
#2. convertCelsius - It will take Fahrenheit and will convert it into Celsiu

class Temprature():
    def convertFahrenheit(self,cel):
        self.cel = cel
        cfahren = 9.0 / 5.0 * self.cel + 32
        print('value in Fahrenheit: %s'%(cfahren))

    def convertCelsius(self,fahrenheit):
        self.fahrenheit = fahrenheit
        celsius=(self.fahrenheit - 32) * 5.0 / 9.0
        print('value in celcius: %s'%(celsius))

obj3 = Temprature()
cel = float(input('enter value in celsius'))
obj3.convertFahrenheit(cel)
fahrenheit = float(input('Enter value into Fahrenheit'))
obj3.convertCelsius(fahrenheit)

#Ques4 Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .
#Make methods to
#1. Display-Display the details.
#2. Update- Update the movie details.
class MovieDetail():
    def __init__(self):
        self.Mname = 'xyz'
        self.artist = 'abcd'
        self.year = '2014'
        self.rating = '*****'
    def display(self):
        print('..Movie detail..')
        print('Movie name: %s \nArtist name: %s \nYear of Release: %s \nRatings: %s'%(self.Mname,self.artist,self.year,self.rating))
    def update(self):
        print('UPDATE \n1.Movie name\n2.Artist name\n3.Year of release\n4.ratings\nENTER YOUR CHOICE')
        a=1
        while(a==1):
            ch = int(input())
            if(ch==1):
                print('Enter movie name')
                self.Mname = input()
            elif(ch==2):
                print('Enter artist name')
                self.artist = input()
            elif(ch==3):
                print('Enter year of release')
                self.year=input()
            elif(ch==4):
                print('Enter ratings')
                self.rating = input()
            else:
                print('Enter valid choice')
            print('Again wanna update? if yes press 1 else 2')
            a = int(input())
m = MovieDetail()
m.display()
m.update()
m.display()

#Ques5 Create a class Expenditure and initialize it with expenditure,savings.Make the following methods.
#1. Display expenditure and savings
#2. Calculate total salary
#3. Display salary
class Expenditure():
    def __init__(self):
        self.expe = 300
        self.savings = 2300
    def display1(self):
        print('Expenditure: %s \n savings: %s'%(self.expe,self.savings))
    def totalSalary(self):
        self.totals = self.savings+self.expe
    def total(self):
        print('total salary %s'%(self.totals))
cal = Expenditure()
cal.display1()
cal.totalSalary()
cal.total()




