#Ques1 create a list with user defined input
x = input('Enter the no of element you want to input ')
list1=[]
print('Enter elements')
for i in range(int(x)):
    a=input()
    list1.append(a)
print(list1)


#Ques2 add a list to list1
list2=['google','apple','facebook','microsoft','tesla']
list1.extend(list2)
print('list1,after adding list2 in it')
print(list1)
object=input('Enter the object which occurance you wanna count in list ')
b=list1.count(object)
print(b)


#Ques3 create a list with no and sort it in ascending order
list3 = [4,8,2,9,1]
print('list3 => ',list3)
list3.sort()
print('After sorting list3 => ',list3)


#Ques4 sorting and merging of two array
array1 = [1,2,3,4]
array2 = [1,7,8,9]
print('array1 => %s \n array2 => %s' % (array1,array2))
c = array1
c.extend(array2)
c.sort()
print("After merging and sorting both the array,new array is:")
print(c)


#Ques5 implimentation of stack LIFO Last in First out
z = input('Enter the no of element you want to push in stack ')
stack=[]
print('Enter elements')
for i in range(int(z)):
    a=input()
    stack.append(a)
print(stack)
for i in range(int(z)):
    a=stack.pop()
    print(a)

#Ques5 implimentation of queue FIFO = First in First out
y = input('Enter the no of element you want to push in queue ')
queue=[]
print('Enter elements')
for i in range(int(y)):
    b=input()
    queue.append(b)
print(queue)
for i in range(int(y)):
    b=queue.pop(0)
    print(b)

#Ques6 count even and odd no of the list
list5 = [1,2,3,4,5,6]
even=0
odd=0
for i in range(6):
    if(list5[i]%2==0):
        even=even+1
    else:
        odd=odd+1
print('count of odd no in list = %d and even = %d' % (even,odd))