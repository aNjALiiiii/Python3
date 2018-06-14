#Ques1 Name and handle the exception occured in the following program:
#a=3
# if a<4:
#    a=a/(a-3)
#     print(a)
try:
    a=3
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
    print("can't divide by Zero")

#Ques2 Name and handle the exception occurred in the following program:
#l=[1,2,3]
#print(l[3])
#Index error will be occur
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print('list Index out of bound')


#Ques3 What will be the output of the following code:
# Program to depict Raising Exception

'''try:
    raise NameError("Hi there")
except NameError:
    print("An exception")
    raise
    
Output will be:

An exception
Traceback (most recent call last):
  File "D:/projects/project1/Assignment13.py", line 28, in <module>
    raise NameError("Hi there")
NameError: Hi there'''

#Ques4 What will be the output of the following code:

 # Function which returns a/b
'''def AbyB(a , b):
    try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print("a/b result in 0")
	else:
		print(c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

Output will be:
-5.0
a/b result in 0'''

#Ques5  Write a program to show and handle following exceptions:
#1. Import Error
#2. Value Error
#3. Index Error

try:
    from _ab import *
    list1=[]
    for i in range(3):
        a=int(input('Enter no'))
        list1.append(a)
    print(list1)
    print(list1[3])
    c=a+b
    print(c)
except ImportError:
    print('cannot find the module')
except ValueError:
    print('value should be integer')
except IndexError:
    print('value not found')

#Ques6 Create a user-defined exception AgeTooSmallError() that warns the user when they
#  have entered age less than 18. The code must keep taking input till the user enters
#  the appropriate age number(less than 18)

class AgeTooSmallError(Exception):
    pass
age=18
while True:
    try:
        age1=int(input("Enter age"))
        if age1 < age:
            raise AgeTooSmallError
        elif(age1>age or age1==age):
            print('Correct')
            break;
    except AgeTooSmallError:
         print("Age is less than 18 , try again")