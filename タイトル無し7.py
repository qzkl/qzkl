# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 22:00:48 2019

@author: nakahashi
"""

def perrin(m=200):
    a,b,c=3,0,2
    result=[]
    while a<m:
        result.append(a)
        a,b,c=b,c,a+b
    print(result)
    

print(perrin())

