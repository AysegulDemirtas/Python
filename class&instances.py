#class - instance - inheritance / OOP
#@coreySchafer/YouTube

import random
import sys
import os

#class is a blueprint to create instances 

'''#Creating class&instances
class Employee:
	pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'corey.schafer@company.com'
emp_1.pay = 5000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'test.user@company.com'
emp_2.pay = 4000

print(emp_1.email)
print(emp_2.email)
#Manually'''

#instead of define each attributes for each instance 

class Employee:

#raise_amount is a Class Variables
#to call class variables, variable name is not enough
#class variables are accessible inside its class with the name classname.varname or self.varname 
	raise_amount = 1.04
	
#define a class var to keep amount of employees.
	num_of_emps = 0
	
	def __init__(self, first, last, pay):
		self.fname= first
		self.lname = last
		self.epay = pay
		self.mail = first + '.' + last + '@company.com'

	#want to increment num_of_emps by 1 whenever a new employee is created
		Employee.num_of_emps += 1	

	def fullname(self):
		return '{} {}'.format(self.fname,self.lname)

	def apply_raise(self):
		#or self.epay = int(self.epay * Employee.raise_amount)
		self.epay = int(self.epay * self.raise_amount)

emp_1 = Employee('Corey','Schafer',5000)
emp_2 = Employee('Test' , 'User' , 4000)

print(emp_1.fname)
print(emp_2.fname)

#we can print manually informations about instances
#or we can organize methods to do this
print ('{} {}'.format(emp_1.fname,emp_1.lname))
print (emp_1.fullname())
print (Employee.fullname(emp_1))

emp_1.apply_raise()
print(emp_1.epay)


print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


#can see elements related with object with __dict__
#we can observe that class variables are created in its class' namespace not instance's
print(emp_1.__dict__)
print(Employee.__dict__)

#can manipulate class variabless for whole class and its instances by calling with its class
Employee.raise_amount = 1.05
print(emp_1.raise_amount)

#can manipulate class variabless for only one instance by calling with instance name
emp_1.raise_amount = 1.06
print(emp_1.raise_amount)
print(emp_2.raise_amount)

#now can see the instance(emp_1) has class variable in its namespace
print(emp_1.__dict__)
print(emp_2.__dict__)

#num_of_emps gives the instances how much in the method __init__ is created
print(Employee.num_of_emps)











































