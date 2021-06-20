# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 15:59:05 2019

@author: nakahashi
"""

class Rectangle:
    recs=[]
    
    def __init__(self,w,l):
        self.width=w
        self.len=l
        self.recs.append((self.width,self.len))
        
    def print_size(self):
        print("{} by {}".format(self.width,self.len))
        
r1=Rectangle(10,24)
r2=Rectangle(20,40)
r3=Rectangle(100,200)

print(Rectangle.recs)

r3.print_size()

class Lion:
    def __init__(self,name):
        self.name=name
        
lion=Lion("Dilbert")
print(lion.name)

class AlwaysPositive:
    def __init__(self,number):
        self.n=number
        
    def __add__(self,other):
        return abs(self.n+other.n)
    
x=AlwaysPositive(-20)
y=AlwaysPositive(10)
z=AlwaysPositive(12)

print(x+z)
