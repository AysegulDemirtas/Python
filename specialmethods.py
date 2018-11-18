#Magic - Dunder : special methods / OOP
#@coreySchafer/YouTube

import random
import sys
import os

'''
magic methods
__ double underscores are called as dunder
'''

class Employee:
	raise_amt = 1.04
	
	def __init__(self, first, last, pay):
		self.first= first
		self.last = last
		self.pay = pay
		self.mail = first + '.' + last + '@email.com'

	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	def apply_raise(self):
		self.epay = int(self.epay * self.raise_amt)

	#repr is a representation of an object's name meaningful for programmer
	def __repr__(self):
		return "Employee('{}', '{}', '{}')".format(self.first,self.last,self.pay)

	#str is a representation of an obj's name meaninful for end-user
	def __str__(self):
		return '{} -{}'.format(self.fullname(), self.mail)


emp_1 = Employee ('Corey' , 'Schafer' , 5000)
emp_2 = Employee ('Test' , 'Employee' , 6000)

print (emp_1)

print(repr(emp_1))
#or print(emp_1.__repr__())

print(str(emp_1))
#or print(emp_1.__str__())


#special methods can be continued...






















