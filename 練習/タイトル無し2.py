# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 00:30:33 2020

@author: nakahashi
"""

prime=[2,3,5,7,11,13]
prime_square=[x**2 for x in prime if x**2>100]
print(prime_square)

multiplication=[i * j for i in range(1,3) for j in range(1,10)]
print(multiplication)

I=4
J=7
mat=[[i*J+j+1 for j in range(J)] for i in range(I)]
print(mat)