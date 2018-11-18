#Property @decorator / OOP
#@coreySchafer/YouTube

import random
import sys
import os

'''
	decorator allows us to define a method
	but we can access it like an attribute
'''

class Employee:

	def __init__(self, first, last):
		self.first= first
		self.last = last

	@property
	def email(self):
		return '{}.{}@email.com'.format(self.first,self.last)

	@property
	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	@fullname.setter
	def fullname(self,name):
		first, last = name.split(' ')
		self.first=first
		self.last=last

	@fullname.deleter
	def fullname(self):
		print('Delete Name!')
		self.first=None
		self.last=None

emp_1 = Employee('Jhon' , 'Wick' )

emp_1.first = 'Jim'

#if don't use @fullname property, this line throws 'can't set attr.' error
emp_1.fullname= 'Corey Schafer'


print(emp_1.first)

#we could take back () afteremail and fullname, thanks to properties. 
print(emp_1.email)
print(emp_1.fullname)


del emp_1.fullname

















