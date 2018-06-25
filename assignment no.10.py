##
#Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.

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
#Q.2- Create a Student class and initialize it with name and roll number. Make methods to :
#1. Display - It should display all informations of the student.


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
#Q.3- Create a Temprature class. Make two methods :
#1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
#2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
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

###
#Q.4- Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .
#Make methods to 
#1. Display-Display the details.
#2. Update- Update the movie details.

class movieDetail():
	def __init__(self,moviename,artistname,year_of_release,rating):
		self.moviename=moviename
		self.artistname=artistname
		self.year_of_release=year_of_release
		self.rating=rating
		
	def display(self):
		print("movie name is:",self.moviename)
		print("artistname name is:",self.artistname)
		print("year of release is:",self.year_of_release)
		print("rating is:",self.rating)
		
	def update(self,moviename,artistname,year_of_release,rating):
		self.moviename=moviename
		self.artistname=artistname
		self.year_of_release=year_of_release
		self.rating=rating
		
t=movieDetail(input("enter any moviename:"),input("enter the name of artist:"),input("enter the release date:"),input("enter the rating of movie"))
t.display()
t.update(input("enter any moviename:"),input("enter the name of artist:"),input("enter the release date:"),input("enter the rating of movie"))
t.display()


#Q.5- Create a class Expenditure and initialize it with expenditure,savings.Make the following methods. 
# 1. Display expenditure and savings 
# 2. Calculate total salary
# 3. Display salary

class expenditure():
	def __init__(self,expenditure,saving):
			self.expenditure=expenditure
			self.saving=saving
	
	def display(self):
		print("enter monthly expenditure",self.expenditure)
		print("enter monthly saving",self.saving)
		
	def calculate(self):
		self.salary=self.expenditure+self.saving
		print("your salary:",self.salary)

a=expenditure(int(input("enter your expenditure:")),int(input("enter your savings:")))
a.display()
a.calculate()