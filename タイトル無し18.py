# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 00:37:31 2019

@author: nakahashi
"""

def sum(n):
    if n==0:
        return 0
    return n+sum(n-1)
    
print(sum(1000))