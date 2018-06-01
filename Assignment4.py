import operator
import collections
#TUPLES
#WAP to create a tuple with different data types and do the following operations
tuple1 = ('1','hello','python','2')
print(tuple1)

#1. find the length of tuple
print('Length of the tuple1 is %d' % (len(tuple1)))

#2. Find largest and smallest element of a tuple
tuple2=(1,2,3,4)
tuple3=('nest','greek')
print('smallest element in tuple2 and tuple3 is : '+ str(min(tuple2))+','+str(min(tuple3)))
print('largest element in tuple2 and tuple3 is : '+ str(max(tuple2))+','+str(max(tuple3)))

#WAP to find the product of all elements of a tuple
mul = 1
for i in range(len(tuple2)):
    mul = mul*tuple2[i]
print('product of the element of tuple2 is : ',mul)

#SETS
#1 calculate difference between two set
#=> The difference() method returns a new set containing all the elements that are in set1 but not set2
set1 = {'a','1','2','d'}
set2 = {'b','c','d'}
print('set1 => %s \nset2 => %s'%(set1,set2))
set_diff = set1-set2
print('difference between set1 and set2 is => ',set_diff)

#2 compare two sets
set3 = {1,2,3}
set4 = {2,3,4,5}
print(set3 ^ set4)

#3 print the result of intersection of two sets
set1 = {'a','1','2','d'}
set2 = {'b','c','d'}
set_inter = set1 & set2
print('Intersection of set1 and set is : ',set_inter)

#dictonary
#1 Create a dictionary to store name and marks of 10 students by user input.
d ={}
print('enter the name and marks of student')
print('NAME MARKS\n')
for i in range(10):
    text = input().split()
    d[text[0]]=text[1]
print(d)

#2 Sort the dictionary created in previous question according to marks.
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print(sorted_d)

#3 Count the number of occurrence of each letter in word "MISSISSIPPI". Store count of every letter with the letter in a dictionary.
result = collections.Counter("MISSISSIPPI")
print(result)


