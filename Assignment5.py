#Question1 Take an input year from user and decide whether it is a leap year or not.
year = int(input("Enter Year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{%d is a leap year"%(year))
       else:
           print("%d is not a leap year"%(year))
   else:
       print("%d is a leap year"%(year))
else:
   print("%d is not a leap year"%(year))

#Question2 Take length and breadth input from user and check whether the dimensions are of square or rectangle.
breadth = int(input("Enter breadth "))
length = int(input("Enter length "))
if(breadth==length):
    print("it is square")
else:
    print("The dimension are of rectangle")

#Question3 Take the input age of 3 people and determine oldest and youngest among them.
print("Enter the age of 3 people")
A = int(input())
B = int(input())
C = int(input())
if(A>B):
    if((A>C)):
        print("%d is oldest"%(A))
    else:
        print("%d is oldest"%(C))
elif(B>C):
    print("%d is oldest"%(B))
else:
    print("%d is oldest"%(C))
d = min(A,B,C)
print("%d is youngest"%(d))


#Question4 Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.

#1. if employee is female, then she will work only in urban areas.
#2. if employee is a male and age is in between 20 to 40 then he may work in anywhere
#3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
#4. And any other input of age should print "ERROR".
print("USER DETAIL\n")
age = int(input("Enter age: "))
sex = str(input("Enter sex(M or F)(M: MALE ,F: FEMALE)"))
m_status = str(input("Marital status :(Y or N ?)"))
if(sex=='F' and age>=20):
    print("Enployee will work only urban areas")
elif((sex=='M')and(age>20 and age<40)):
    print("Employee may work anywhere")
elif((sex=='M')and(40<age<60)):
    print("Employee will work urban area only")
else:
    print("Oops!!!! Error....Enter valid age")

#Question5 A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user
# for quantity Suppose, one unit will cost 100. Judge and print total cost for user.
quantity = int(input("Enter the purchased quantity"))
cost = quantity*100
if(cost>1000):
    discount = cost*10/100
else:
    discount = 0
print("total cost for user is : %d"%(cost-discount))



