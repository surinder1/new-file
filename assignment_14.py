#Q.1- Write a Python program to read last n lines of a file

# f=open('hhh.txt','r')
# s=int(input("any thing"))
# z=f.readlines()
# while s:
	# print(z[-s])
	# s=s-1

	
#Q.2- Write a Python program to count the frequency of words in a file. 
# c=0
# f=open('hhh.txt','r')
# for line in f:
	# words=line.split()
	# c +=len(words)
# print(c)


#Q3 Write a Python program to copy the contents of a file to another file

# f=open('hhh.txt','r')
# s=open('new.txt','w')
# for line in f:
	# s.write(line)
# z=f.readline()
# print(z)


#Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.

f=open('hhh.txt','r'):
    a=f.readlines()
	n=len(a)
	print(a)

s=open('new.txt','r'):
	z=s.readlines()
	w=len(s)
	print(s)
i=0
for x in range(min(n,w)):
	print(a[i]+z[i])
	i++
	
	
#Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and 
#then store it to another file.
import os
import random
list2=[]
n=int(input('How many random numbers:'))
os.remove("random.txt")
with open("random.txt","w") as afile:	
	for i in range(n):	#insert n random number as per user
		list2.append(random.randint(1, 100))
	#print(list2,"#")
	for x in range(len(list2)):		#write numbers in file
		afile.write(str(list2[x])+"\n")		#"\n"-print number line by line
	#afile.seek(0)
with open("random.txt","r+") as f1:
	list1=f1.readlines()
	for i in range(len(list1)):
		list1[i]=int(list1[i])	#type casting
	list1.sort()	#sorting
	#print(list1)
with open("random_sorted.txt","w") as f2:
	for x in list1:
		f2.write(str(x)+"\n")
		



