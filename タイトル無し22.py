# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 14:41:05 2019

@author: nakahashi
"""

prime=[x for x in range(1,11)]
prime_square=[x**2 for x in prime]

print(prime)
print(prime_square)

multiplication=[i*j for i in range(1,3) for j in range(1,10)]
print(multiplication)