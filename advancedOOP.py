#date : 24.05.2016
#author: Ayşegül Demirtaş
#id : PY004
#tag : dJango and python or Views
#mission : learn python , decorator/ lexical scope/ OOP

import random
import sys
import os

'''Object Oriented Programming'''
#Object class definition
class Animal:
	__name=None
	__height=0
	__weight=0
	__sound=0

	def set_name(self, name):
		self.__name=name

	def get_name(self):
		return self.__name

#Constructors
	def __init__(self, name, height, weight, sound ):
		self.__name=name
		self.__height=height
		self.__weight=weight
		self.__sound=sound

	def get_type(self):
		print("Animal")

	def toString(self):
		return "{} is {} cm tall and {} kilograms and says {}".format(self.__name, self.__height, self.__weight, self.__sound)

cat = Animal('Whiskers',33,10,'Meow')
print (cat.toString())

#Inheritance

class Dog(Animal):
	__owner= None
	
	def __init__(self, name, height, weight, sound, owner):
		self.__owner= owner
	
#	super(Dog,self).__init__(name, height, weight, sound)

	def set_owner(self,owner):
		self.__owner= owner

	def get_owner(self):
		return self.__owner

	def get_type(self):
		print("Dog")

	def toString2(self):
		return "{} is {} cm tall and {} kilograms and says {} and its owner is {}".format(self.__name, self.__height, self.__weight, self.__sound, self.__owner )

husky = Dog('Spot' , 42 , 27 , 'Ruff' , 'Derek' )
print (husky.toString2())














