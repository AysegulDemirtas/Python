#@decorators 
#@coreySchafer/YouTube

import random
import sys
import os


'''decorator is a function that takes another function as an argument 
as some kind of functionality and then returns another function
without changing the source code o the original function
'''

def decorator_function(original_function):
	def wrapper_function():
		print('wrapper exxecuted this beore {}'.format(original_function.__name__))
		return original_function()
	return wrapper_function


def display():
	print('display function ran')

decorated_display = decorator_function(display)

decorated_display()
