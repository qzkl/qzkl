# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 15:30:58 2019

@author: nakahashi
"""

numbers=list(range(1,11,2))

    
functions=[sum,max,min]

for func in functions:
    print("Function:{},Result:{}".format(func.__name__,func(numbers)))