##

class circle:
	def __init__(self,radius):
		self.r=radius
	 
	def get_area(self):
		print(3.14*self.r*self.r)
	def get_circumfrance(self):
		print(2*3.14*self.r)

a=circle(7)
a.get_area()
a.get_circumfrance()


##
class student():
	def __init__(self,name,roll_number):
		self.name=name
		self.roll_number=roll_number
	
	def display(self):
		print("your name is",self.name)
		print("your roll number is",self.roll_number)
		
a=student(input("enter your name"),int(input("enter your roll_number")))
a.display()


###

class temperature():
	def __init__(self,fahrenheit,celsius):
		self.fahrenheit=fahrenheit
		self.celsius=celsius
	def convertfahrenhiet(self):
		fahrenheit=1.8*self.celsius+32
		print("temperature in fahrenheit",fahrenheit)
	
	def convertcelsius(self):	
		celsius=(5*(self.fahrenheit-32))/9
		print("temperature in celsius",celsius)

a=temperature(int(input("fahrenheit:")),int(input("fahrenheit:")))
a.convertcelsius()
a.convertfahrenhiet()