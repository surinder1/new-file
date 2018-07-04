#Q.1- Name and handle the exception occured in the following program: 

#a=3
#if a<4:
#	a=a/(a-3)
#	print(a)

# try:
	# a=3
	# if a<4:
		# a=a/(a-3)
		# print(a)

# except Exception:
	# print("Hello")
	
# Q.2- Name and handle the exception occurred in the following program: 
# l=[1,2,3]
# print(l[3])

# try:
	# l=[1,2,3]
	# print(l[3])
	
# except Exception:
	# print("element is not present")
	
	
#Q.4- What will be the output of the following code:

 # Function which returns a/b
# def AbyB(a,b):
	# try:
		# c = ((a+b) / (a-b))
	# except ZeroDivisionError:
		# print("a/b result in 0")
	# else:
		# print(c)

# Driver program to test above function
# AbyB(2.0, 3.0)
# AbyB(3.0, 3.0)

	
#Q.3- What will be the output of the following code:

# Program to depict Raising Exception
 
# try:
    # raise NameError("Hi there")  # Raise Error
# except NameError:
#   print "An exception"
#   raise  # To determine whether the exception was raised or not


# Q.4- What will be the output of the following code:

 # Function which returns a/b
# def AbyB(a , b):
	# try:
		# c = ((a+b) / (a-b))
	# except ZeroDivisionError:
		# print("a/b result in 0")
	# else:
		# print(c)

# Driver program to test above function
# AbyB(2.0, 3.0)
# AbyB(3.0, 3.0)

#Q.5- Write a program to show and handle following exceptions: 
#1. Import Error
#2. Value Error
#3. Index Error


# import error

# try:
	# import surinder
# except Exception as e:
	# print(e)

# value error

# try:
	# a=int("ab")
# except Exception as a:
	# print(a)
	
#index error

# a=[1,2,3]
# print(a(5))


#Q.6- Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18. The code must keep taking input till the user enters the appropriate age number(less than 18). 

class AgeTooSmallError(Exception):
	pass
try:
	while True:
		age=int(input("enter the age"))
		if age<18:
			print("age is less than 18",age)
		else:
			raise AgeTooSmallError("age is above 18")
except AgeTooSmallError as e:
	print(e)
	
		

