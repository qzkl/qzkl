# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:49:08 2019

@author: nakahashi
"""

square=[]

for i in range(1,6):
    i=i**2
    square.append(i)

square2=[36,49]
square.extend(square2)
square.insert(2,7)

print(square)

square.remove(7)

print(square)

print(square.pop(1))

print(square)

print(square.count(16))
