import datetime
import time
import math
import os
#Ques1 What is Time Tuple?

#Many of Python's time functions handle time as a tuple of 9 numbers, as shown below −

#Index	Field	            Values
#0	    4-digit year	    2008
#1	    Month	            1 to 12
#2	    Day	                1 to 31
#3	    Hour	            0 to 23
#4	    Minute	            0 to 59
#5	    Second	            0 to 61 (60 or 61 are leap-seconds)
#6	    Day of Week	        0 to 6 (0 is Monday)
#7	    Day of year	        1 to 366 (Julian day)
#8	    Daylight savings	-1, 0, 1, -1 means library determines DST

#Ques2 Write a program to get formatted time.
localtime = time.asctime( time.localtime(time.time()) )
print("Local current time :", localtime)

#Ques3 Extract month from the time.
d = datetime.date.today()
print(d)
print(d.month)

#Ques4 Extract day from the time.
d = datetime.date.today()
print(d.day)

#Ques5 Extract date (ex : 11 in 11/01/2021) from the time.
d = datetime.date.today()
print(d)
print(d.day)

#Ques6 Write a program to print time using localtime method.
localtime = time.localtime(time.time())
print("Local current time :", localtime)


#Ques7 Find the factorial of a number input by user using math package functions.
no = int(input('enter the no which factorial you wanna find'))
print('fact is %d'%(math.factorial(no)))


#Ques8 Find the GCD of a number input by user using math package functions.
num1,num2 = int(input('enter two no for finding gcd')),int(input())
print('gcd is: %d'%(math.gcd(num1,num2)))


#Ques9 Use OS package and do the following tasks:
#1. Get current working directory.
#2. Get the user environment.
#1.
c = os.getcwd()
print('current working directory: %s'%(c))
#2.
print(os.environ)
