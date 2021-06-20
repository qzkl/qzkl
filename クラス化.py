# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:14:46 2019

@author: nakahashi
"""

class Rectangle:
    def __init__(self,w,l):
        self.width=w
        self.len=l
        
    def area(self):
        return self.width*self.len
    
    def change_size(self,w,l):
        self.width=w
        self.len=l
        
rectangle=Rectangle(10,20)
print(rectangle.area())
rectangle.change_size(20,40)
print(rectangle.len)

