#!/usr/bin/python

class Parent:

    def __init__(self):
        print ( 'Parent constructor' )
        self.x = 0
        self.y = 0

    def setValues(self, a, b):
        self.x = a
        self.y = b

    def printValues(self):
        print ('The value of x is' , self.x )
        print ('The value of y is' , self.y )

    def __privateMethod(self):
        print ('Parent private method')

class Child(Parent):

    def __init__(self):
        Parent.__init__(self)
        print ( 'Child constructor')
        self.z = 0

    def setValues(self, a, b, c ):
        Parent.setValues (self, a, b)
        self.z = c

    def printValues(self):
        Parent.printValues(self)
        print ('The value of z is', self.z )

def main():

    child = Child()

    child.printValues()
    child.setValues ( 100, 200, 300 )
    child.printValues()

    #child.__privateMethod() #if uncommented gives an error as private methods aren't inherited by child
main()


