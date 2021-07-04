# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 14:55:04 2019

@author: nakahashi
"""

prime=[2,3,5,7,11,13]

prime_square=[x**2 for x in prime if x**2 > 100]

print(prime_square)

abc=["x is 2" if x==2 else "X is 1" if x==1 else "other" for x in range(3)]
print(abc)