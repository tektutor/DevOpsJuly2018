#!/usr/bin/python

class MyClass:

    def __init__( self ):
        print ( "MyClass constructor" )
        self.x = 0
        self.y = 0

    def setValues ( self, firstValue, secondValue ):
        self.x = firstValue
        self.y = secondValue

    def printValues ( self ):
        print ('Value of x is ' + str ( self.x ) )
        print ('Value of y is ' + str ( self.y ) )


def main():

    obj1 = MyClass()

    obj1.printValues()
    obj1.setValues ( 100, 200 )
    obj1.printValues()

    obj2 = MyClass()

    obj2.printValues()
    obj1.setValues ( 1000, 2000 )
    obj1.printValues()

main()
