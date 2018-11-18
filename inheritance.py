#inheritance / OOP
#@coreySchafer/YouTube

import random
import sys
import os

'''
inheritance allows us to inherit attributes and methods from a parent class
subclasses get all the functionality of its parent class
can overwrite new functionalities without
affecting the parent class
'''
class Employee:
	raise_amt = 1.04
	
	def __init__(self, first, last, pay):
		self.fname= first
		self.lname = last
		self.epay = pay
		self.mail = first + '.' + last + '@company.com'

	def fullname(self):
		return '{} {}'.format(self.fname,self.lname)

	def apply_raise(self):
		self.epay = int(self.epay * self.raise_amt)

#in this format, class A(B) means that class A interits rom B = A is child,B is parent
class Developer(Employee):
	raise_amt = 1.10

#if want to add more attributes into subclass, need to define its own __init__ method 
	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first,last,pay)
		#or Employee.__init__(self,first,last,pay)
		self.prog_lang=prog_lang

dev_1 = Developer('Corey','Schafer',5000 ,'Python')
dev_2 = Developer('Test' , 'User' , 4000 , 'Java')

print(dev_1.mail)
print(dev_2.mail)

print(dev_1.epay)
dev_1.apply_raise()
print(dev_1.epay)

print(dev_1.prog_lang)


