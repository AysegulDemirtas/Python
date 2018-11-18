#date : 23.05.2016
#author: Ayşegül Demirtaş
#id : PY001
#tag : my very first python code
#mission : learn python basics

import random
import sys
import os

#of course first thing to do printing helloWorld!
print ("hello World!")

#single-line command
quote = "abc"
print ("my single line quote is :" , quote )


'''it gives
multi-line
command 
ability'''
multi_line_quote = ''' I 
can
write
so 
many
words. 
'''
print("my multi line quote is:" , multi_line_quote)


#variables have no type requiring, interesting...
name = "Ayşegül"
print (name)

#+ - * / ** // % arithmetic operation...
num1 = 2
num2 = 10
print ( "Number1 is :" , num1 , "Number2 is : " , num2 ) 

summ = num1 + num2
print ("sum is " , summ )
casc = quote + multi_line_quote
print( "You can also use + for cascading strings...", casc )

extract = num2 - num1
print ( "Number2 - Number1 is :",  extract )

multi = num1 * num2
print ("Multiply is :" , multi )
print( "You can also use * for repeating strings...", name *5 )

divide = num2 / num1
print ("Division is :" , divide )

expo = num1 ** num2
print ("Exponentian Number2 of Number1 is :" , expo )

dobdiv = num2 // num1
print ("double divide o Num1//Num2 is :" , dobdiv) 

modulus = num2 % num1
print ("Mod Number2 % Number1 is :" , modulus )

#user input
print( "Speak to me :")
input1 = sys.stdin.readline()
print( input1 )
input2 = input('\nSpeak more..')
print ("Thanks to say : %s " % input2 )









