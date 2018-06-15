from collections import Counter
import random
'''Save the following passage in .txt file. Solve the below questions using this file.
“Atticus said to Jem one day, “I’d rather you shot at tin cans in the backyard, but I know you’ll go after birds.
Shoot all the blue jays you want, if you can hit ‘em, but remember it’s a sin to kill a mockingbird.”
That was the only time I ever heard Atticus say it was a sin to do something, and I asked Miss Maudie about it.
“Your father’s right,” she said. “Mockingbirds don’t do one thing except make music for us to enjoy.
They don’t eat up people’s gardens, don’t nest in corn cribs, they don’t do one thing but sing their hearts out for us.
That’s why it’s a sin to kill a mockingbird.” – Harper Lee, To Kill a Mockingbird
Q.1- Write a Python program to read last n lines of a file
Q.2- Write a Python program to count the frequency of words in a file.
Q.3- Write a Python program to copy the contents of a file to another file
Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.
Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers
and then store it to another file.'''

fd = open("ab.txt","w")
line = ["Atticus said to Jem one day, “I’d rather you shot at tin cans in the backyard, but I know you’ll go after birds.\n",
"Shoot all the blue jays you want, if you can hit ‘em, but remember it’s a sin to kill a mockingbird.”\n",
"That was the only time I ever heard Atticus say it was a sin to do something, and I asked Miss Maudie about it.\n",
"“Your father’s right,” she said. “Mockingbirds don’t do one thing except make music for us to enjoy.\n",
"They don’t eat up people’s gardens, don’t nest in corn cribs, they don’t do one thing but sing their hearts out for us.\n",
"That’s why it’s a sin to kill a mockingbird.” – Harper Lee, To Kill a Mockingbird]\n"]
fd.writelines(line)
fd.close()

#Ques1
try:
    f=open("ab.txt","r")
    n=int(input('Enter no of last n line which you want to read'))
    for lines in (f.readlines()[-n:]):
        print(lines,end='')
except:
    print('Error')

#Ques2
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("ab.txt"))

#Ques3
fd1 = open("ab.txt","r")
fd2 = open("cd.txt","w")
for line in (fd1.readlines()[:]):
    fd2.writelines(line)
fd2.close()
fd1.close()
fd2 = open("cd.txt","r")
for line in (fd2.readline()):
    print(fd2.readline())
#or
with open("test.txt") as f:
    with open("out.txt", "w") as f1:
        for line in f:
            f1.write(line)

#Ques4
with open('ab.txt') as fh1, open('test.txt') as fh2:
    for line1, line2 in zip(fh1, fh2):
        # line1 from abc.txt, line2 from test.txtg
        print(line1+line2)

#Ques5
afile = open("Random.txt", "w" )
for i in range(10):
    line=random.randint(1, 100)
    afile.write(str(line)+"\n")
    print(line)

afile.close()
data = []
with open("Random.txt",'r') as myfile:
    for line in myfile:
        data.extend(map(int, line.split(',')))
print(sorted(data))
with open("new.txt","w") as afile:
    afile.write(str(sorted(data)))
