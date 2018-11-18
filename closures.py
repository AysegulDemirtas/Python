#@closures
#@coreySchafer/YouTube

import random
import sys
import os

'''
Closure is a record storing a function together with an environment
A mapping associating each free variable of the function with the value
or storage location to which the name was bound when the closure was created
Allows the function to access those captured variables through the closure's reference to them
-even when the function is invoked outside their scope 
'''

def outer_function():
	message = 'Hi'

	def inner_function():
		print(message)

	return inner_function()

my_func = outer_function()
print(my_func)

my_func = outer_function 
my_func()
my_func()
my_func()

#closure is an inner func that remembers and has access to 
#variables in the local scope in which it was created
#even after the outer function is finished executing

def ou_func(msg):
	mssg = msg

	def inn_func():
		print(mssg)

	return inn_func

hi_func = ou_func('Hi')
hello_func = ou_func('Hello')

hi_func()
hello_func()









