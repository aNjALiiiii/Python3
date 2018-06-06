#Ques1 Create a function to calculate the area of a sphere by taking radius from user.
def sphere(r):
    pi = 3.14
    area = 4*pi*(r)**2
    return area
radius = float(input('Enter the value of the radius of sphere'))
a=sphere(radius)
print('area of sphere is: %s'%(a))


#Ques2 Write a function “perfect()” that determines if parameter number is a perfect number.
# Use this function in a program that determines and prints all the perfect numbers between 1 and 1000.
#[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself),
# sum to the number. E.g., 6 is a perfect number because 6=1+2+3].
def perfect(num):
    list=[]
    sum=0
    for i in range(1,num):
        if(num%i==0):
            list.append(i)
        for j in range(len(list)):
            sum=sum+list[j]
        if(sum==num):
            print(num)
print('perfect no\'s are:' )
for k in range(2,1001):
    perfect(k)


#Ques3  Print multiplication table of 12 using recursion.
def tables(n, t=1):
    if t == 11:
        return
    print(str(n) + " x " + str(t) + " = " + str(n * t))
    tables(n, t + 1)

tables(12)


#Ques4 Write a function to calculate power of a number raised to other ( a^b ) using recursion.
def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result is:",power(base,exp))


#Ques5  Write a function to find factorial of a number but also store the factorials calculated in a dictionary
def factorial(no):
    fact=1
    for m in range(1,no+1):
        fact = fact*m
    return fact
number = int(input('enter the no, which factorial you wanna find'))
print('factorial is %s '%(factorial(number)))
d={}
d[number]=factorial(number)
print(d)

