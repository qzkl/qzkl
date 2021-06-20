# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 23:48:12 2019

@author: nakahashi
"""

def my_func(x):
    x.append(1)
    
my_list=[0,1,2,3]
my_func(my_list)

print(my_list)