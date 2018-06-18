# leap year
year=int(input("enter any year:"))	

if year%4==0:
	if year%100==0:
	
		if year%400==0:
			print("enterd year is a leap year")
		else:
			print("not a leap year")
	else:
		print("entered year is a leap year")
else:
	print("not a leap year")
 	
	
x=int(input("enter leghth of square"))
y=int(input("enter breadth of square"))
if 	x==y:
	print("it is a square")
else:
	print("it is a rectengle")
	
x=1
y=2
z=3

if x>y:
	if x>z:
		print(x,"is oldest")
	else:
		print(z,"is oldest")
else:
	if y>z:
		print(y,"is oldest")
	else:
		print(z,"is oldest")
		

if x<y:
	if x<z:
		print(x,"is youngest")
	else:
		print(z,"is youngest")
else:
	if y<z:
		print(y,"is youngest")
	else:
		print(z,"is youngest")
	


point=int(input("enter your point between 1 to 200:"))
if point<=50:
	print("Sorry! no prize this time")
elif point>=51 and point<=150:
	print("congratulations! you won a wooden dog")
elif point>=151 and point<=180:
	print("congratulations! you won a book")
elif point>=181 and point<=200:
	print("congratulations! you won a chocolate")
else:
	print("please enter the point between 1 to 200")
	
print("price of 1 unit=100")
unit=int(input(("enter the units you want to purchase: ")))
price=unit*100
if price>1000:
 	print("you have to pay:",price-price/10)
else: 
	print("you have to pay",price)








	
		
		