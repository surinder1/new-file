#1
l=[]
for x in range(10):
	l.append(int(input("enter any number")))

for x in l:
	print(x)
#2	
i=1
while i<3:
	print("hello world")
#3
l=[]
for x in range(5):
	l.append(int(input("enter any number")))
print(l)

s=[]
for x in range(5):
	s.append(l[x]**2)
print(s)
#4
l=[1,2,2.3,"mohit",7,"surinder",87,"rohit"]
li=[]
ls=[]
lf=[]

for x in l:
	if type(x)==int:
		li.append(x)
	elif type(x)==str:
		ls.append(x)
	elif type(x)==float:
		lf.append(x)
print(li)
print(ls)
print(lf)
#5
even=[]
odd=[]
for x in range(1,101):
	if x%2==0:
		even.append(x)
	else:
		odd.append(x)
print("even:",even)
print("odd",odd)
#6
for i in range(5):
	for j in range(i):
		print("x",end="")
	print()
#7	
d={}
for x in range(5):
	key=input("enter the key")
	value=input("enter the value")
	d[key]=value
print(d)
#8
l=[]
for x in range(6):
	l.append(int(input("enter any number:")))
search=int(input("enter the number you want to search:"))
print(l)
flag=0
for x in l:
	if x==search:
		l.remove(x)
		flag=1
		break
if flag==0:
	print("number not found")
print(l)
	