#!/bin/python

import math
import os
import random
import re
import sys



class Rectangle:
    def __init__(self,b,l):
        self.b= b
        self.l= l
    def area(self):
        return self.b*self.l

class Circle:
    def __init__(self,r):
        self.r= r
    def area(self):
            return math.pi*(self.r**2)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(raw_input())
    queries = []
    for _ in xrange(q):
        args = raw_input().split()
        shape_name, params = args[0], map(int, args[1:])
        if shape_name == "rectangle":
            a, b = params[0], params[1]
            shape = Rectangle(a, b)
        elif shape_name == "circle":
            r = params[0]
            shape = Circle(r)
        else:
            raise ValueError("invalid shape type")
        fptr.write("%.2f\n" % shape.area())
    fptr.close()
