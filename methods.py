#classmethods - staticmethods / OOP
#@coreySchafer/YouTube

import random
import sys
import os

#Creating class&instances
'''
class methods may be used as alternative constructers
you can use these class methods in order to 
provide multi-ways of creating objects
'''

'''
regular methods automatically pass the instance(self) as the first argument 
class methods authomatically pass the class(cls) as the first argument
static methods don't pass anything authomatically
'''

class Employee:
	raise_amt = 1.04
	num_of_emps = 0
	
	def __init__(self, first, last, pay):
		self.fname= first
		self.lname = last
		self.epay = pay
		self.mail = first + '.' + last + '@company.com'
	#want to increment num_of_emps by 1 whenever a new employee is created
		Employee.num_of_emps += 1	


	#set_raise_amt is a class method
	@classmethod
	def set_raise_amt(cls,amount):
		cls.raise_amt =amount

	@classmethod
	def from_string(cls,emp_str):
		first, last, pay = emp_str.split('-')	
		return cls(first,last,pay)	

	@staticmethod
	def is_workday(day):
		if day.weekday()==5 or day.weekday()==6:
			return False
		return True

'''
if you don't acces the instance or the class anywhere
within the function then use static method
'''

emp_1 = Employee('Corey','Schafer',5000)
emp_2 = Employee('Test' , 'User' , 4000)

print (Employee.raise_amt)
print (emp_1.raise_amt)
print (emp_2.raise_amt)

Employee.set_raise_amt(1.05)
#emp_1.set_raise_amt(1.05) does do same thing either  

print (Employee.raise_amt)
print (emp_1.raise_amt)
print (emp_2.raise_amt)

emp_str_1 = 'Jhon-Doe-7000'
emp_str_2 = 'Steve-Smith-3000'
emp_str_3 = 'Jane-Doe-9000'

#string splittig
first, last, pay = emp_str_1.split('-')

new_emp_1 = Employee(first, last, pay)

print(new_emp_1.mail)
print(new_emp_1.epay)

emp_str_4 = 'Grace-Shirley-10000'
emp_str_5 = 'Kennen-Shuriman-5000'

new_emp_2 = Employee.from_string(emp_str_4)
print(new_emp_2.mail)
print(new_emp_2.epay)

import datetime
my_date = datetime.date(2016 , 7 , 10 )
print(Employee.is_workday(my_date))




















