# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 14:05:24 2019

@author: nakahashi
"""

stack=[]
stack.append(1)
print("stack:", stack)
stack.append(2)
stack.append(2)
stack.append(2)
print("stack num:", len(stack))
print("stack:", stack)
print("pop 1st value:", stack.pop())
print("pop 2nd value:", stack.pop())