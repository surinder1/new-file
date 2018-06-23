def a():
	x=int(input("enter the radius"))
	r=3.14*x*x 
	print(r)
a()


def perfect(num):
	result=0
	for x in range(1,num):
		if num%x==0:
			result=result+x
	if result==num:
		print("perfect number:",num)
	
for x in range(1,1001):
	perfect(x)
	


def rectangle(x,y):
	if y<=10:
		t=x*y
		print(t)
		y+=1
		rectangle(x,y)
rectangle(12,1)
	


def power(a,b):
	if b==1:
		return a
	else:
		p=a*power(a,b-1)
a=int(input("enter base: "))
b=int(input("power of base:"))
print(power(a,b))



# def fact(x):
	if x==1 or x==0:
		return 1
	else:
		f=x*fact(x-1)
		return f
d{}
for x in range(5):
	num=int(input("enter any number:"))
	a=fact(num)
	fact(num)=f
	print(f)


	
	

	
		

	
	