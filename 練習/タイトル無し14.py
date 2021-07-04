# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 17:37:10 2019

@author: nakahashi
"""

def makecounter(n=0):
#    n=0
    def count():
        nonlocal n
        n+=1
        return n
    return count

counter=makecounter(3)

print(counter())
print(counter())
print(counter())
print(counter())

    
