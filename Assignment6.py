#Ques1 Take 10 integers from user and print it on screen.
list =[]
print("Enter integers")
for i in range(10):
    a=input()
    list.append(a)
for i in range(10):
    print(list[i])

#Ques2 Write an infinite loop.An infinite loop never ends. Condition is always true.
'''j = 1;
while(j>0):
    print("infinite loop")'''

#Ques3 Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.
list1=[]
list2=[]
n=int(input('Enter the no of integers you wanna store in list'))
print("Enter "+str(n)+" integers")
for i in range(n):
    b=input()
    list1.append(b)
for i in range(n):
    list2.append((int(list1[i]))**2)
print(list2)

#Ques4 From a list containing ints, strings and floats, make three lists to store them separately
list3=['hello',4,'python',12.0,2,2.5,]
print("list = > %s"%(list3))
list4=[]
list5=[]
list6=[]
for i in range(len(list3)):
    if(type(list3[i])==str):
        list4.append(list3[i])
    elif(type(list3[i])==int):
        list5.append(list3[i])
    elif(type(list3[i])==float):
        list6.append(list3[i])
print(list4)
print(list5)
print(list6)

#Ques5 Using range(1,101), make a list containing only prime numbers.
list7 = []
for num in range(1, 101):
    for i in range(2, num):
        if (num % i == 0):
            break
        else:
            list7.append(num)
            break
print(list7)

#Ques6 Print the following patterns:
#*
#**
#***
#****
for i in range (1,6):
    print('*'*i)

#Ques7 Create a user defined dictionary and get keys corresponding to the value using for loop.
d ={}
print('enter keys and values of the dictionary')
print('key | value\n')
for i in range(2):
    text = input().split()
    d[text[0]]=text[1]
print(d)

#Ques8 Take inputs from user to make a list.
# Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.
list9=[]
print("Enter elements of the list")
for i in range(5):
    c=int(input())
    list9.append(c)

key = int(input('Enter the key which you want to del.'))
if key in list9:
    index1 = list9.index(key)
    print(index1)
    del list9[index1]
else:
    print('element not found in the list')
print(list9)