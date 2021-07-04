# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 22:58:44 2020

@author: nakahashi
"""

class MyClass1:
    def __init__(self,text):
        self.text=text
        
a=MyClass1('abc')
b=MyClass1('ggg')
c=MyClass1('brf')

print(a.text)
print(b.text)
print(c.text)

a.text='xyz'
print(a.text)

a.new_text='another text'
print(a.new_text)

class MyClass2:
    common_text="class value"
    
print(MyClass2.common_text)