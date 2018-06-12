#QUES1:  Create a threading process such that it sleeps for 5 seconds and then prints out a message.
import time
import threading
import _thread
from threading import Thread

def sleepMe():
     print("Thread is sleeping for 5 sec",threading.currentThread().getName())
     time.sleep(5)
     print("Thread is awake now",threading.currentThread().getName())

t=Thread(target=sleepMe,args=())
t.start()

#QUES2: Make a thread that prints numbers from 1-10, waits for 1 sec between
i=1
def printNo(i):
    time.sleep(1)
    print('number is %s'%(i))
try:
     _thread.start_new_thread(printNo,(i))
except:
    print('unable to start thread')
while(i<=10):
    pass
    i=i+1

#QUES3:Make a list that has 5 elements.Create a threading process that prints the 5 elements
# of the list with a delay of multiple of 2 sec between each display.
#Delay goes like 2sec-4sec-6sec-8sec-10sec
list1 = [1,2,3,4,5]

def printList(i):
    j=i*2
    time.sleep(j)
    print("list element is: %s" % (list1[i-1]))

for i in range(1,6):
    th = Thread(target=printList, args=(i,))
    th.start()

#QUES4:Call factorial function using thread.
n = int(input('Enter the no which factorial you want to find'))
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact1 = fact*i
    print(fact1)
try:
    _thread.start_new_thread(factorial,(n))
except:
    print('unable to start thread')

pass

