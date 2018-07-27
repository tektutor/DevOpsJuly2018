#!/usr/bin/python

def add(firstValue, secondValue): 
           print( ' Inside add function ' )
           return firstValue + secondValue


x = 100
y = 200

print ("The result of " + str(x) + " + " + str(y) + " is " + str( add( 100, 200 ) ) )
print ("The result of 100.5 + 200.9 is " , add( 100.5, 200.9 ) )
print ("The result of Hello + World is " , add( 'Hello ', 'World' ) )
